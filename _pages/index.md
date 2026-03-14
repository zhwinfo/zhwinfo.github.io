---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
  - /index_
  - /index_.html
---

<button onclick="topFunction()" id="toTopBtn" title="toTop">to TOP</button>

<span class='anchor' id='index'></span>

# 📄 About
I am currently an Associate Professor at the School of Artificial Intelligence, <a href='https://en.wikipedia.org/wiki/Beijing_Normal_University' target="_blank">Beijing Normal University</a>.

My team focuses on creating humanoid agents that learn and act in 3D worlds, specifically through the capture and generation of realistic human motion, appearance, and behavior. We work closely with <a href="https://scholar.google.com/citations?user=ogXIdlYAAAAJ&hl=en" target="_blank">Prof. Yebin Liu</a>.

I am looking for self-motivated Ph.D./Master students with strong research interests in 3D Vision, Computer Graphics, and Embodied AI.

<div class="profile-actions">
<a href='https://ai.bnu.edu.cn/xygk/szdw/fgj/9b9ed1de20d3445fbdd4a57b72b2b885.htm' target="_blank" class="btn btn--small profile-link">中文简介</a>
</div>
<p class="profile-actions-text">
欢迎北师大校内外同学联系实习、申请硕士/博士研究生<span class="profile-actions-inline"><a shape="rect" href="javascript:togglebib('recruitment')" class="btn btn--small togglebib recruitment-link">招生说明</a></span>
</p>
<!-- <strong style="color:red;">2025年入学本人剩余名额：1名博士；课题组合作指导剩余名额：1名硕士；</strong><br /> -->
<strong style="color:red;">本校本科同学可随时进组科研实习，有意保研的大二/大三同学请尽早联系</strong>
<!-- <br />
<a href='https://mp.weixin.qq.com/s/6Cguf6p2ucyk-yKk5Tv1_Q' target="_blank">欢迎选择保研北京师范大学人工智能学院！</a> -->

<div class='text-box' id="recruitment">
<pre xml:space="preserve">
招收硕士/博士研究生（含：学硕/专硕/学博/专博），
研究方向：三维视觉、图形学、具身智能、构建在三维世界中学习与行动的人形智能体；
随时欢迎了解咨询，请尽可能提前线下/远程实习；
由于名额有限，有意通过夏令营/保研/考研等方式进组的同学【均需要提前联系】；

由于申请邮件较多，抱歉无法逐一回复，符合条件的候选同学会在三天内收到回复邮件以进一步联系；
近两年情况的参考申请条件：
保研：有CCF-A类论文已发表/录用/在投(需附上论文PDF)/完整的Demo作品（需演示效果）
考研：暂无参考条件（侧重数学/408/机试成绩和实践能力）
博士：有CCF-A类论文已发表/录用且有完整的Demo作品
</pre>
</div>
<!-- 
申请链接：<a href="https://zhanghongwen.cn/admission" target="_blank">https://zhanghongwen.cn/admission</a> -->

<span class='anchor' id='-research'></span>
# 📚 Research 

<a href='https://github.com/HongwenZhang' target='_blank'><img src='https://img.shields.io/github/stars/HongwenZhang?label=GitHub%20Stars&style=social'></a>

<a href='https://scholar.google.com/citations?user=6z0m_ZMAAAAJ&hl=en' target='_blank'><img src='https://img.shields.io/badge/dynamic/json?label=Google%20Scholar%20Citations&query=total_citations&url=https%3A%2F%2Fcse.bth.se%2F~fer%2Fgooglescholar-api%2Fgooglescholar.php%3Fuser%3D6z0m_ZMAAAAJ&logo=googlescholar&style=social'></a>
<!-- <a href='https://scholar.google.com/citations?user=6z0m_ZMAAAAJ&hl=en' target='_blank'><img src='https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fzhang-hongwen%2Fzhang-hongwen.github.io@gs-data%2Fgs_data_shieldsio.json&style=social&label=Google%20Scholar%20Citations'></a> -->

<span class='anchor' id='-motion-capture'></span>

🎉&ensp; 5 paper accepted to <strong style="color:red;">CVPR/ICRA/TVCG/CHI 2026</strong>

🎉&ensp; 10 paper accepted to <strong style="color:red;">TPAMI/TVCG/CVPR/ICCV/NeurIPS/AAAI 2025</strong>

🎉&ensp; 8 paper accepted to <strong style="color:red;">CVPR/SIGGRAPH 2024</strong>

## 🚩 Preprints
<div style="clear: both;">

   {% for p in site.data.preprint.items %}
   {% include card_item.html p=p show_ccf=false %}
   {% endfor %}

</div>

<div class="view-toggle-bar">
  <a href='/?view=topic#-research' class='view-toggle active-view' data-view='topic'><i class="fas fa-layer-group"></i><span>View by Topic</span></a>
  <a href='/?view=year#-research' class='view-toggle' data-view='year'><i class="fas fa-calendar-alt"></i><span>View by Year</span></a>
  <a href='publications.html' class='view-toggle'><i class="fas fa-list"></i><span>All Publications</span></a>
</div>

<div id="view-topic">
  <div style="display: flex;" class="tab-container" id="research-tab-container">
    <button class="highlight_research_tab" onclick="toggle_research_vis('#-motion-capture', this)"  id="tab_a">Motion Capture</button>
    <button class="research_tab" onclick="toggle_research_vis('#-motion-understanding', this); toggleContent()"  id="tab_b">Motion Generation</button>
    <button class="research_tab" onclick="toggle_research_vis('#-human-reconstruction', this); toggleContent()"  id="tab_c">Human Reconstruction</button>
    <button class="research_tab" onclick="toggle_research_vis('#-animatable-avatar', this); toggleContent()"  id="tab_d">Animatable Avatar</button>
  </div>
  <div class="placeholder" id="all_tab_place"></div>

  <h2 id="-motion-capture">🚩 Human/Hand/Face/Full-body Motion Capture</h2>

  {% include list_by_topic_cards.html topic="Motion Capture" featured_only=true show_ccf=false %}

  <div class="content" onclick="expandContent()" id='content_mask'>

    {% include list_by_topic_cards.html topic="Motion Capture" featured_only=false show_ccf=false %}

    <div class="placeholder" id="tab_b_place"></div>

    <span class='anchor' id='-motion-understanding'></span>
    <h2 id="-motion-understanding">🚩 Motion Understanding and Generation</h2>

    {% include list_by_topic_cards.html topic="Motion Generation" featured_only=false show_ccf=false %}

    <div class="placeholder" id="tab_c_place"></div>

    <span class='anchor' id='-human-reconstruction'></span>
    <h2 id="-human-reconstruction">🚩 Clothed Human Reconstruction/Rendering</h2>

    {% include list_by_topic_cards.html topic="Clothed Human" featured_only=false show_ccf=false %}

    <div class="placeholder" id="tab_d_place"></div>

    <span class='anchor' id='-animatable-avatar'></span>
    <h2 id="-animatable-avatar">🚩 Animatable Avatar</h2>

    {% include list_by_topic_cards.html topic="Animatable Avatar" featured_only=false show_ccf=false %}

    <span class='anchor' id='-cloth-modeling'></span>
    <!-- <h2 id="-cloth-modeling">🚩 Animatable Clothed Human Modeling</h2> -->
    <div class="placeholder" id="end_place"></div>


    <h2> <a class="paper" onclick="_gaq.push(['_trackEvent', 'Pub', 'Download', 'more']);" href="publications.html">Click to View the Full List of Publications</a></h2>

    <div class="tooltip">Click to Load More Publications</div>
  </div>

  <!-- <div class="more-btn" onclick="toggleContent()">Click to Load More Publications</div> -->

  <div class="toggle-btn" onclick="toggleContent()">
    <div class="more-btn">Click to Load More Publications on Clothed Human/Avatar Modeling</div>
  </div>

</div><!-- end of view-topic -->

<div id="view-year" style="display:none;">
{% include list_by_year_cards.html show_ccf=false %}
</div>

<script>
(function() {
  function showView(view) {
    var topic = document.getElementById('view-topic');
    var year = document.getElementById('view-year');
    if (!topic || !year) return;
    if (view === 'year') {
      topic.style.display = 'none';
      year.style.display = 'block';
    } else {
      topic.style.display = 'block';
      year.style.display = 'none';
      view = 'topic';
    }
    var toggles = document.querySelectorAll('.view-toggle');
    for (var i = 0; i < toggles.length; i++) {
      var el = toggles[i];
      if (el.getAttribute('data-view') === view) {
        el.classList.add('active-view');
      } else {
        el.classList.remove('active-view');
      }
    }
  }

  function initViewFromQuery() {
    try {
      var params = new URLSearchParams(window.location.search);
      var view = params.get('view');
      if (view !== 'year' && view !== 'topic') {
        view = 'topic';
      }
      showView(view);
    } catch (e) {
      showView('topic');
    }
  }

  document.addEventListener('DOMContentLoaded', function() {
    var toggles = document.querySelectorAll('.view-toggle');
    for (var i = 0; i < toggles.length; i++) {
      toggles[i].addEventListener('click', function(e) {
        var view = this.getAttribute('data-view');
        if (!view) {
          return;
        }
        e.preventDefault();
        if (view !== 'year' && view !== 'topic') {
          view = 'topic';
        }
        showView(view);
        try {
          var url = new URL(window.location.href);
          url.searchParams.set('view', view);
          window.history.replaceState({}, '', url.toString());
        } catch (err) {}
      });
    }
    initViewFromQuery();
  });
})();
</script>


<span class='anchor' id='-honor-award'></span>

# 🎖️ Honor & Awards

<div class='paper-box' id="CAST-YESS"><div class='paper-box-image'><div><img src='https://topscinet.com/static/images/logo2.jpg' alt='WorldTopScientists' width="100%" loading="eager"></div></div>
<div class='paper-box-text' markdown="1">
<a ><strong>Stanford University’s List of "World's Top 2% Scientists"</strong></a><br />
斯坦福全球前2%顶尖科学家榜单, by Stanford & Elsevier<br />
</div>
</div>

<div class='paper-box' id="CAST-YESS"><div class='paper-box-image'><div><img src='images/cast_yess.jpg' alt='青托工程' width="100%" loading="eager"></div></div>
<div class='paper-box-text' markdown="1">
<a ><strong>中国科协青年人才托举工程, Young Elite Scientist Sponsorship Program by CAST</strong></a><br />
     China Association for Science and Technology (CAST)<br />
</div>
</div>

<div class='paper-box' id="CAS-D"><div class='paper-box-image'><div><img src='images/award-CAS.jpg' alt='优博证书' width="100%" loading="eager"></div></div>
<div class='paper-box-text' markdown="1">
<a ><strong>中国科学院优秀博士学位论文, CAS Outstanding Doctoral Dissertation</strong></a><br />
    授予单位: 中国科学院, Awarded by the Chinese Academy of Sciences (CAS)<br />
</div>
</div>

<span class='anchor' id='-academic-services'></span>

# 📑 Academic Services

Technical Papers Committee for SIGGRAPH (Asia)

<span class='anchor' id='-collaborators'></span>

# 🌏 Collaborators

I have been fortunately advised by and working with:<br />
<a href="https://www.au.tsinghua.edu.cn/en/info/1096/3380.htm" target="_blank">Prof. Yebin Liu 刘烨斌 (Tsinghua University)</a>,<br />
<a href="http://www.cbsr.ia.ac.cn/users/znsun" target="_blank">Prof. Zhenan Sun 孙哲南 (Institute of Automation, CAS)</a>,<br />
<a href="https://wlouyang.github.io" target="_blank">Prof. Wanli Ouyang 欧阳万里 (Shanghai AI Lab)</a>,<br />
and <a href="https://scholar.google.com/citations?hl=en&user=6z0m_ZMAAAAJ#d=gsc_md_cod&t=1714397341598&u=%2Fcitations%3Fview_op%3Dlist_colleagues%26hl%3Den%26json%3D%26user%3D6z0m_ZMAAAAJ%23t%3Dgsc_cod_lc" target="_blank">More</a>.

<!-- PostDoc, <strong>Tsinghua University</strong> (Advisor: <a href="https://liuyebin.com" target="_blank">Prof. Yebin Liu</a>)<br /> 
Ph.D., <strong>Institute of Automation, Chinese Academy of Sciences</strong> (Advisor: <a href="http://www.cbsr.ia.ac.cn/users/znsun" target="_blank">Prof. Zhenan Sun</a>)<br /> 
Visiting Student, <strong>The University of Sydney</strong> (Advisor: <a href="https://wlouyang.github.io" target="_blank">Prof. Wanli Ouyang</a>)<br /> 
B.E., <strong>South China University of Technology</strong> -->

<br />
<br />
<br />

<a ><img style="height:0;" src='//clustrmaps.com/map_v2.png?cl=080808&w=109&t=n&d=YixTrW_BMdr5L3rb__AgAOkCfxEXKHagTEWHnPVvoAI&co=ffffff&ct=808080'></a>
