# -*- coding: utf-8 -*-
"""生成闲鱼项目用的 SVG 占位商品图（本地文件，离线可用）。
后期想换成真实图片时，把 HTML 里 img:'img/goods/g01.svg' 改成 'img/1.jpg' 即可。"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'goods')
os.makedirs(OUT, exist_ok=True)

# (文件名, emoji, 说明文字, 渐变色1, 渐变色2)
ITEMS = [
    ('g01', '\U0001F9F4', '美妆护肤',   '#ffd9e8', '#ffb3c8'),
    ('g02', '\U0001F527', '汽车配件',   '#d6e4ff', '#a9c2ff'),
    ('g03', '\U0001F6E0', '文玩摆件',   '#f6e0b5', '#e0c08a'),
    ('g04', '\U0001F9E3', '保暖耳套',   '#dff1ff', '#a9d8f5'),
    ('g05', '\U0001F6F9', '平衡训练板', '#d9f7e6', '#a6e6c3'),
    ('g06', '\U0001F3A3', '海钓装备',   '#d9ecff', '#9fc9f2'),
    ('g07', '\U0001F6B2', '自行车贴纸', '#ffeed6', '#ffd39b'),
    ('g08', '\U0001F94B', '运动垫',     '#e6e0ff', '#c0b3ff'),
    ('g09', '\u2699\uFE0F', '五金焊材',   '#e3e8ec', '#b9c4cc'),
    ('g10', '\U0001F50C', '电子元件',   '#dff5ef', '#a8e6d6'),
    ('g11', '\U0001F388', '打气筒',     '#ffe3f0', '#ffb8d9'),
    ('g12', '\U0001F5BC', '装饰摆画',   '#f2e6d8', '#d8bf9c'),
    ('g13', '\U0001F34A', '手动榨汁机', '#ffeccf', '#ffd08a'),
    ('g14', '\U0001F436', '宠物用品',   '#e8f7d9', '#bfe6a0'),
    ('g15', '\U0001F6E2', '汽车油液',   '#ffdcdc', '#ffabab'),
    ('g16', '\U0001F9E5', '雨衣外套',   '#e0eaff', '#b0c6f5'),
    ('g17', '\U0001F9F0', '上门服务',   '#e9f0ff', '#c2d4f7'),
    ('g18', '\u2712\uFE0F', '钢笔文具',   '#f0e4ff', '#cdb0f5'),
    ('g19', '\U0001F5C3', '老物件',     '#f5e6cf', '#d6b78c'),
    ('g20', '\U0001F699', '车载装备',   '#dcecf7', '#a8c9e0'),
    # 彩色卡片里的 2 个商品预览位
    ('t1', '\U0001F457', '美衣',   '#fff3c4', '#ffe08a'),
    ('t2', '\U0001F9E5', '外套',   '#ffe6c9', '#ffc78a'),
    ('t3', '\U0001F458', '手办',   '#d8ffe6', '#9ff0be'),
    ('t4', '\U0001F9F8', '潮玩',   '#c9ffe9', '#8fe8cf'),
    ('t5', '\U0001F4F1', '手机',   '#d9ecff', '#a2ccf7'),
    ('t6', '\U0001F3A7', '耳机',   '#cfe6ff', '#96c4f2'),
    ('t7', '\U0001F39F', '卡券',   '#ffe0ef', '#ffabcf'),
    ('t8', '\U0001F37F', '零食',   '#ffe9d6', '#ffc49b'),
    # 彩色卡片左侧插画位
    ('i1', '\U0001F6CD', '',      '#fff0a8', '#ffdc4d'),
    ('i2', '\U0001F380', '',      '#bdf5d5', '#79e0aa'),
    ('i3', '\U0001F4F7', '',      '#bfe2ff', '#7fbcfa'),
    ('i4', '\U0001F4B3', '',      '#ffc9e4', '#ff92c6'),
]

TPL = ('<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">'
       '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
       '<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/>'
       '</linearGradient></defs>'
       '<rect width="400" height="400" fill="url(#g)"/>'
       '<circle cx="200" cy="185" r="132" fill="#ffffff" opacity="0.35"/>'
       '<text x="200" y="232" font-size="150" text-anchor="middle" '
       'font-family="Segoe UI Emoji,Apple Color Emoji,Noto Color Emoji">{emo}</text>'
       '<text x="200" y="345" font-size="30" text-anchor="middle" fill="#8a8a8a" '
       'font-family="Microsoft YaHei,sans-serif">{label}</text>'
       '</svg>')

for name, emo, label, c1, c2 in ITEMS:
    with open(os.path.join(OUT, name + '.svg'), 'w', encoding='utf-8') as f:
        f.write(TPL.format(c1=c1, c2=c2, emo=emo, label=label))

print('done:', len(ITEMS), 'files ->', OUT)
