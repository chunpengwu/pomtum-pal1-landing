# -*- coding: utf-8 -*-
"""把落地页 emoji 图标换成简洁 SVG 线稿图标"""
import re

path = r"C:\Users\calmr\Downloads\pomtum-live\index.html"
html = open(path, encoding="utf-8").read()

# emoji -> SVG 线稿(24x24, stroke=currentColor, 简洁风)
SVGS = {
    "🎒": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="9" width="12" height="11" rx="2.5"/><path d="M9 9V7a3 3 0 0 1 6 0v2"/><path d="M12 13v3"/></svg>',  # 口袋手机
    "🚀": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4.5 10.5 9 11l4 4 .5 4.5L22 11z"/><path d="M13 2l4 4"/><path d="M9 11l-4.5 4.5L3 21l5.5-1.5L13 15"/></svg>',  # 火箭
    "📡": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="2"/><path d="M7.8 7.8a6 6 0 0 0 0 8.4"/><path d="M16.2 7.8a6 6 0 0 1 0 8.4"/><path d="M4.9 4.9a10 10 0 0 0 0 14.2"/><path d="M19.1 4.9a10 10 0 0 1 0 14.2"/></svg>',  # 信号
    "🤖": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="8" width="14" height="11" rx="3"/><path d="M12 8V5"/><path d="M9 4.5h6"/><circle cx="9.5" cy="13" r="1"/><circle cx="14.5" cy="13" r="1"/><path d="M9 17h6"/></svg>',  # 机器人
    "🐧": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="14" rx="2.5"/><path d="m7 9 2 2-2 2"/><path d="m12 9 2 2-2 2"/><path d="M17 13h1"/></svg>',  # 终端
    "✉️": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3 7 9 6 9-6"/></svg>',  # 信封
    "🔒": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',  # 锁
    "✓": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m4 12.5 5 5L20 6.5"/></svg>',  # 对勾
}

# 1. 替换 .icon 里的 emoji
def replace_icon(m):
    emoji = m.group(1)
    svg = SVGS.get(emoji)
    return svg if svg else m.group(0)

html = re.sub(r'<span class="icon">([^<]+)</span>', replace_icon, html)

# 2. 按钮里的 ✉️ → SVG(保留文字)
html = html.replace(
    '<button type="submit" class="submit-btn">✉️ Notify me at launch</button>',
    '<button type="submit" class="submit-btn"><svg style="width:16px;height:16px;vertical-align:-3px;margin-right:6px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3 7 9 6 9-6"/></svg>Notify me at launch</button>'
)

# 3. 表单脚注 🔒 → SVG
html = html.replace(
    '<p class="form-foot">🔒 We only use this to notify you about PomTum Pal 1.</p>',
    '<p class="form-foot"><svg style="width:13px;height:13px;vertical-align:-2px;margin-right:5px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>We only use this to notify you about PomTum Pal 1.</p>'
)

# 4. 成功对勾 → SVG
html = html.replace('<div class="check">✓</div>', '<div class="check"><svg style="width:22px;height:22px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m4 12.5 5 5L20 6.5"/></svg></div>')

# 5. console.log 去 emoji
html = html.replace("console.log('📋 Lead captured:', data)", "console.log('Lead captured:', data)")

open(path, "w", encoding="utf-8").write(html)

# 6. 更新 .icon CSS: 从 font-size 改成 svg 尺寸
html = open(path, encoding="utf-8").read()
html = html.replace(
    ".mini-card .icon{font-size:28px;display:block;margin-bottom:12px}",
    ".mini-card .icon{display:block;margin-bottom:12px}.mini-card .icon svg{width:30px;height:30px;color:var(--accent)}"
)
html = html.replace(
    ".dual-card .icon{font-size:28px;display:block;margin-bottom:12px}",
    ".dual-card .icon{display:block;margin-bottom:12px}.dual-card .icon svg{width:30px;height:30px;color:var(--accent)}"
)
open(path, "w", encoding="utf-8").write(html)

# 验证: 没有 emoji 了
import re
emoji_pattern = re.compile('[\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F\u2705\u2714\u2713]')
left = [(i+1, m.group()) for i, line in enumerate(html.split(chr(10)), 1) for m in emoji_pattern.finditer(line)]
print("剩余 emoji:", left if left else "无 ✅")
print("SVG 图标数:", html.count("<svg"))
print("完成!")
