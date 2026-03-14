// Simple signaling server using HTTP + SSE, no external deps
const http = require('http');
const url = require('url');

const PORT = process.env.PORT ? parseInt(process.env.PORT, 10) : 5001;
const HOST = '0.0.0.0';

const rooms = new Map(); // roomId -> { offer, answer, subscribers: Set<res> }

function getRoom(id) {
  if (!rooms.has(id)) {
    rooms.set(id, { offer: null, answer: null, subscribers: new Set() });
  }
  return rooms.get(id);
}

function sendEvent(res, type, payload) {
  try {
    res.write(`event: ${type}\n`);
    res.write(`data: ${JSON.stringify(payload)}\n\n`);
  } catch (_) {
    // Ignore broken pipe
  }
}

function setCORS(res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

function parseBody(req) {
  return new Promise((resolve) => {
    let data = '';
    req.on('data', (chunk) => (data += chunk));
    req.on('end', () => {
      try {
        const json = JSON.parse(data || '{}');
        resolve(json);
      } catch {
        resolve({});
      }
    });
  });
}

const server = http.createServer(async (req, res) => {
  setCORS(res);
  const parsed = url.parse(req.url, true);
  const pathname = parsed.pathname || '/';
  const roomId = (parsed.query && String(parsed.query.room || '').trim()) || '';

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    return res.end();
  }

  if (!roomId && (pathname === '/offer' || pathname === '/answer' || pathname === '/events' || pathname === '/status')) {
    res.writeHead(400, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ error: 'room required' }));
  }

  if (pathname === '/events' && req.method === 'GET') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      Connection: 'keep-alive',
    });
    const room = getRoom(roomId);
    room.subscribers.add(res);

    // Send current state if exists
    if (room.offer) sendEvent(res, 'offer', room.offer);
    if (room.answer) sendEvent(res, 'answer', room.answer);

    req.on('close', () => {
      room.subscribers.delete(res);
    });
    return; // keep connection open
  }

  if (pathname === '/offer' && req.method === 'POST') {
    const body = await parseBody(req);
    if (!body || !body.sdp || !body.type) {
      res.writeHead(400, { 'Content-Type': 'application/json' });
      return res.end(JSON.stringify({ error: 'invalid offer' }));
    }
    const room = getRoom(roomId);
    room.offer = body;
    // Notify subscribers
    for (const sub of room.subscribers) sendEvent(sub, 'offer', room.offer);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ ok: true }));
  }

  if (pathname === '/answer' && req.method === 'POST') {
    const body = await parseBody(req);
    if (!body || !body.sdp || !body.type) {
      res.writeHead(400, { 'Content-Type': 'application/json' });
      return res.end(JSON.stringify({ error: 'invalid answer' }));
    }
    const room = getRoom(roomId);
    room.answer = body;
    for (const sub of room.subscribers) sendEvent(sub, 'answer', room.answer);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ ok: true }));
  }

  if (pathname === '/status' && req.method === 'GET') {
    const room = getRoom(roomId);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ hasOffer: !!room.offer, hasAnswer: !!room.answer }));
  }

  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'not found' }));
});

server.listen(PORT, HOST, () => {
  console.log(`Signaling server listening on http://${HOST}:${PORT}`);
});

