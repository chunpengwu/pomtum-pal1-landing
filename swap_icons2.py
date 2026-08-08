# -*- coding: utf-8 -*-
"""把手绘 SVG 换成 Feather 图标库标准路径"""
import re

path = r"C:\Users\calmr\Downloads\pomtum-live\index.html"
html = open(path, encoding="utf-8").read()

def feather(path_d, vb="0 0 24 24", sw=2):
    return f'<svg viewBox="{vb}" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{path_d}</svg>'

# Feather 标准图标
ICONS = {
    "smartphone": feather('<rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line>'),
    "zap": feather('<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>'),
    "wifi": feather('<path d="M5 12.55a11 11 0 0 1 14.08 0"></path><path d="M1.42 9a16 16 0 0 1 21.16 0"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12.01" y2="20"></line>'),
    "cpu": feather('<rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line>'),
    "terminal": feather('<polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line>'),
    "mail": feather('<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline>'),
    "lock": feather('<rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>'),
    "check": feather('<polyline points="20 6 9 17 4 12"></polyline>', sw=2.4),
}

# 1. mini-card 图标(按顺序: 口袋/闪电/信号)
mc = re.findall(r'<span class="icon">.*?</span>', html, re.S)
order_mc = ["smartphone", "zap", "wifi"]
for i, tag in enumerate(mc[:3]):
    html = html.replace(tag, f'<span class="icon">{ICONS[order_mc[i]]}</span>', 1)

# 2. dual-card 图标(按顺序: 机器人→cpu, 企鹅→terminal)
dc = re.findall(r'<span class="icon">.*?</span>', html, re.S)
order_dc = ["cpu", "terminal"]
for i, tag in enumerate(dc[:2]):
    html = html.replace(tag, f'<span class="icon">{ICONS[order_dc[i]]}</span>', 1)

# 3. 按钮信封 / 脚注锁 / 成功对勾 —— 整个 svg 替换
html = re.sub(r'<svg style="width:16px;height:16px[^>]*>.*?</svg>', ICONS["mail"].replace('<svg ', '<svg style="width:16px;height:16px;vertical-align:-3px;margin-right:6px" ', 1), html, flags=re.S)
html = re.sub(r'<svg style="width:13px;height:13px[^>]*>.*?</svg>', ICONS["lock"].replace('<svg ', '<svg style="width:13px;height:13px;vertical-align:-2px;margin-right:5px" ', 1), html, flags=re.S)
html = re.sub(r'<svg style="width:22px;height:22px[^>]*>.*?</svg>', ICONS["check"].replace('<svg ', '<svg style="width:22px;height:22px" ', 1), html, flags=re.S)

open(path, "w", encoding="utf-8").write(html)

# 验证
import re as _re
sizes = _re.findall(r'<svg[^>]*>', html)
print("svg 总数:", len(sizes))
print("含手绘路径标记(火箭尖角)的:", html.count('L13 2'))
print("完成 ✅")
