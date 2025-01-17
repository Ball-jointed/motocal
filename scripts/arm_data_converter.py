import csv
import inspect
import json
import os
import re
from collections import OrderedDict

skillnamelist = OrderedDict()

# Normal Skills / 通常スキル ################################################################################################

# normal L and LL
skillnamelist["normalLLM"] = {
    u"紅蓮の攻刃III": "fire",
    u"霧氷の攻刃III": "water",
    u"地裂の攻刃III": "earth",
    u"乱気の攻刃III": "wind",
    u"天光の攻刃III": "light",
    u"奈落の攻刃III": "dark"
}

skillnamelist["normalLL"] = {
    u"紅蓮の攻刃II": "fire",
    u"霧氷の攻刃II": "water",
    u"地裂の攻刃II": "earth",
    u"乱気の攻刃II": "wind",
    u"天光の攻刃II": "light",
    u"奈落の攻刃II": "dark"
}

# Inferno's Insignia is usually treated as a large atk up
skillnamelist["normalL"] = {
    u"紅蓮の攻刃": "fire",
    u"霧氷の攻刃": "water",
    u"地裂の攻刃": "earth",
    u"乱気の攻刃": "wind",
    u"天光の攻刃": "light",
    u"奈落の攻刃": "dark",
    u"紅蓮の呪印": "fire"
}

# normalM
skillnamelist["normalM"] = {
    u"業火の攻刃": "fire",
    u"渦潮の攻刃": "water",
    u"大地の攻刃": "earth",
    u"竜巻の攻刃": "wind",
    u"雷電の攻刃": "light",
    u"憎悪の攻刃": "dark"
}

# normalS
skillnamelist["normalS"] = {
    u"火の攻刃": "fire",
    u"水の攻刃": "water",
    u"土の攻刃": "earth",
    u"風の攻刃": "wind",
    u"光の攻刃": "light",
    u"闇の攻刃": "dark"
}

skillnamelist["normalHPLL"] = {
    u"紅蓮の守護II": "fire",
    u"霧氷の守護II": "water",
    u"地裂の守護II": "earth",
    u"乱気の守護II": "wind",
    u"天光の守護II": "light",
    u"奈落の守護II": "dark"
}

skillnamelist["normalHPL"] = {
    u"紅蓮の守護": "fire",
    u"霧氷の守護": "water",
    u"地裂の守護": "earth",
    u"乱気の守護": "wind",
    u"天光の守護": "light",
    u"奈落の守護": "dark"
}

skillnamelist["normalHPM"] = {
    u"業火の守護": "fire",
    u"渦潮の守護": "water",
    u"大地の守護": "earth",
    u"竜巻の守護": "wind",
    u"雷電の守護": "light",
    u"憎悪の守護": "dark"
}

skillnamelist["normalHPS"] = {
    u"火の守護": "fire",
    u"水の守護": "water",
    u"土の守護": "earth",
    u"風の守護": "wind",
    u"光の守護": "light",
    u"闇の守護": "dark"
}

skillnamelist["normalNiteL"] = {
    u"紅蓮の二手": "fire",
    u"霧氷の二手": "water",
    u"地裂の二手": "earth",
    u"乱気の二手": "wind",
    u"天光の二手": "light",
    u"奈落の二手": "dark"
}

skillnamelist["normalNiteM"] = {
    u"業火の二手": "fire",
    u"渦潮の二手": "water",
    u"大地の二手": "earth",
    u"竜巻の二手": "wind",
    u"雷電の二手": "light",
    u"憎悪の二手": "dark"
}

skillnamelist["normalNiteS"] = {
    u"火の二手": "fire",
    u"水の二手": "water",
    u"土の二手": "earth",
    u"風の二手": "wind",
    u"光の二手": "light",
    u"闇の二手": "dark"
}

skillnamelist["normalCriticalLL"] = {
    u"紅蓮の技巧II": "fire",
    u"霧氷の技巧II": "water",
    u"地裂の技巧II": "earth",
    u"乱気の技巧II": "wind",
    u"天光の技巧II": "light",
    u"奈落の技巧II": "dark"
}

skillnamelist["normalCriticalL"] = {
    u"紅蓮の技巧": "fire",
    u"霧氷の技巧": "water",
    u"地裂の技巧": "earth",
    u"乱気の技巧": "wind",
    u"天光の技巧": "light",
    u"奈落の技巧": "dark"
}

skillnamelist["normalCriticalM"] = {
    u"業火の技巧": "fire",
    u"渦潮の技巧": "water",
    u"大地の技巧": "earth",
    u"竜巻の技巧": "wind",
    u"雷電の技巧": "light",
    u"憎悪の技巧": "dark"
}

skillnamelist["normalCriticalS"] = {
    u"火の技巧": "fire",
    u"水の技巧": "water",
    u"土の技巧": "earth",
    u"風の技巧": "wind",
    u"光の技巧": "light",
    u"闇の技巧": "dark"
}

skillnamelist["normalHaisuiL"] = {
    u"紅蓮の背水": "fire",
    u"霧氷の背水": "water",
    u"地裂の背水": "earth",
    u"乱気の背水": "wind",
    u"天光の背水": "light",
    u"奈落の背水": "dark"
}

skillnamelist["normalHaisuiM"] = {
    u"業火の背水": "fire",
    u"渦潮の背水": "water",
    u"大地の背水": "earth",
    u"竜巻の背水": "wind",
    u"雷電の背水": "light",
    u"憎悪の背水": "dark"
}

skillnamelist["normalHaisuiS"] = {
    u"火の背水": "fire",
    u"水の背水": "water",
    u"土の背水": "earth",
    u"風の背水": "wind",
    u"光の背水": "light",
    u"闇の背水": "dark"
}

# Although stamina can be handled normally at present, if ~ star skill is to be treated as a separate frame, it is necessary to make it different skill
skillnamelist["normalKonshinLL"] = {
    u"紅蓮の渾身II": "fire",
    u"霧氷の渾身II": "water",
    u"地裂の渾身II": "earth",
    u"乱気の渾身II": "wind",
    u"天光の渾身II": "light",
    u"奈落の渾身II": "dark",
    u"青星の渾身II": "water",
    u"白星の渾身II": "light"
}

skillnamelist["normalKonshinL"] = {
    u"紅蓮の渾身": "fire",
    u"霧氷の渾身": "water",
    u"地裂の渾身": "earth",
    u"乱気の渾身": "wind",
    u"天光の渾身": "light",
    u"奈落の渾身": "dark",
    u"青星の渾身": "water",
    u"白星の渾身": "light"
}

skillnamelist["normalKonshinM"] = {
    u"業火の渾身": "fire",
    u"渦潮の渾身": "water",
    u"大地の渾身": "earth",
    u"竜巻の渾身": "wind",
    u"雷電の渾身": "light",
    u"憎悪の渾身": "dark"
}

skillnamelist["normalKonshinS"] = {
    u"火の渾身": "fire",
    u"水の渾身": "water",
    u"土の渾身": "earth",
    u"風の渾身": "wind",
    u"光の渾身": "light",
    u"闇の渾身": "dark"
}

skillnamelist["normalHiouL"] = {
    u"紅蓮の秘奥": "fire",
    u"霧氷の秘奥": "water",
    u"地裂の秘奥": "earth",
    u"乱気の秘奥": "wind",
    u"天光の秘奥": "light",
    u"奈落の秘奥": "dark"
}

skillnamelist["normalHiouM"] = {
    u"業火の秘奥": "fire",
    u"渦潮の秘奥": "water",
    u"大地の秘奥": "earth",
    u"竜巻の秘奥": "wind",
    u"雷電の秘奥": "light",
    u"憎悪の秘奥": "dark"
}

skillnamelist["normalHiouS"] = {
    u"火の秘奥": "fire",
    u"水の秘奥": "water",
    u"土の秘奥": "earth",
    u"風の秘奥": "wind",
    u"光の秘奥": "light",
    u"闇の秘奥": "dark"
}

skillnamelist["normalHigoS"] = {
    u"火の庇護": "fire",
    u"水の庇護": "water",
    u"土の庇護": "earth",
    u"風の庇護": "wind",
    u"光の庇護": "light",
    u"闇の庇護": "dark"
}

skillnamelist["normalKamuiL"] = {
    u"紅蓮の神威": "fire",
    u"霧氷の神威": "water",
    u"地裂の神威": "earth",
    u"乱気の神威": "wind",
    u"天光の神威": "light",
    u"奈落の神威": "dark"
}

skillnamelist["normalKamuiM"] = {
    u"業火の神威": "fire",
    u"渦潮の神威": "water",
    u"大地の神威": "earth",
    u"竜巻の神威": "wind",
    u"雷電の神威": "light",
    u"憎悪の神威": "dark"
}

skillnamelist["normalKamui"] = {
    u"火の神威": "fire",
    u"水の神威": "water",
    u"土の神威": "earth",
    u"風の神威": "wind",
    u"光の神威": "light",
    u"闇の神威": "dark"
}

# Musou: Attack up + double atk rate
skillnamelist["normalMusouLL"] = {
    u"業火の無双II": "fire",
    u"渦潮の無双II": "water",
    u"地裂の無双II": "earth",
    u"竜巻の無双II": "wind",
    u"雷電の無双II": "light",
    u"憎悪の無双II": "dark"
}
skillnamelist["normalMusouM"] = {
    u"業火の無双": "fire",
    u"渦潮の無双": "water",
    u"大地の無双": "earth",
    u"竜巻の無双": "wind",
    u"雷電の無双": "light",
    u"憎悪の無双": "dark"
}

skillnamelist["normalRanbuM"] = {
    u"業火の乱舞": "fire",
    u"渦潮の乱舞": "water",
    u"大地の乱舞": "earth",
    u"竜巻の乱舞": "wind",
    u"雷電の乱舞": "light",
    u"憎悪の乱舞": "dark"
}

skillnamelist["normalRanbuS"] = {
    u"火の乱舞": "fire",
    u"水の乱舞": "water",
    u"土の乱舞": "earth",
    u"風の乱舞": "wind",
    u"光の乱舞": "light",
    u"闇の乱舞": "dark"
}

skillnamelist["normalSetsunaLL"] = {
    u"紅蓮の刹那II": "fire",
    u"霧氷の刹那II": "water",
    u"地裂の刹那II": "earth",
    u"竜巻の刹那II": "wind",
    u"天光の刹那II": "light",
    u"奈落の刹那II": "dark"
}

skillnamelist["normalSetsunaL"] = {
    u"紅蓮の刹那": "fire",
    u"霧氷の刹那": "water",
    u"地裂の刹那": "earth",
    u"竜巻の刹那": "wind",
    u"天光の刹那": "light",
    u"奈落の刹那": "dark"
}

skillnamelist["normalSetsuna"] = {
    u"業火の刹那": "fire",
    u"渦潮の刹那": "water",
    u"大地の刹那": "earth",
    u"竜巻の刹那": "wind",
    u"雷電の刹那": "light",
    u"憎悪の刹那": "dark"
}

skillnamelist["normalSetsunaS"] = {
    u"火の刹那": "fire",
    u"水の刹那": "water",
    u"土の刹那": "earth",
    u"風の刹那": "wind",
    u"光の刹那": "light",
    u"闇の刹那": "dark"
}

# 守護 + 技巧
skillnamelist["normalJinkaiS"] = {
    u"火の刃界": "fire",
    u"水の刃界": "water",
    u"土の刃界": "earth",
    u"風の刃界": "wind",
    u"光の刃界": "light",
    u"闇の刃界": "dark"
}

# Grace
skillnamelist["normalOntyouM"] = {
    u"業火の恩寵": "fire",
    u"渦潮の恩寵": "water",
    u"大地の恩寵": "earth",
    u"竜巻の恩寵": "wind",
    u"雷電の恩寵": "light",
    u"憎悪の恩寵": "dark"
}

skillnamelist["normalOntyouS"] = {
    u"火の恩寵": "fire",
    u"水の恩寵": "water",
    u"土の恩寵": "earth",
    u"風の恩寵": "wind",
    u"光の恩寵": "light",
    u"闇の恩寵": "dark"
}

skillnamelist["normalSanteL"] = {
    u"紅蓮の三手": "fire",
    u"霧氷の三手": "water",
    u"地裂の三手": "earth",
    u"乱気の三手": "wind",
    u"天光の三手": "light",
    u"奈落の三手": "dark"
}

skillnamelist["normalSanteM"] = {
    u"業火の三手": "fire",
    u"渦潮の三手": "water",
    u"大地の三手": "earth",
    u"竜巻の三手": "wind",
    u"雷電の三手": "light",
    u"憎悪の三手": "dark"
}

skillnamelist["normalSanteS"] = {
    u"火の三手": "fire",
    u"水の三手": "water",
    u"土の三手": "earth",
    u"風の三手": "wind",
    u"光の三手": "light",
    u"闇の三手": "dark"
}

skillnamelist["normalKatsumiM"] = {
    u"業火の克己": "fire",
    u"渦潮の克己": "water",
    u"大地の克己": "earth",
    u"竜巻の克己": "wind",
    u"雷電の克己": "light",
    u"憎悪の克己": "dark"
}

skillnamelist["normalKatsumiS"] = {
    u"火の克己": "fire",
    u"水の克己": "water",
    u"土の克己": "earth",
    u"風の克己": "wind",
    u"光の克己": "light",
    u"闇の克己": "dark"
}

skillnamelist["normalKatsumokuS"] = {
    u"紅蓮の括目": "fire",
    u"霧氷の括目": "water",
    u"地裂の括目": "earth",
    u"乱気の括目": "wind",
    u"天光の括目": "light",
    u"奈落の括目": "dark"
}

skillnamelist["normalHissatsuL"] = {
    u"紅蓮の必殺": "fire",
    u"霧氷の必殺": "water",
    u"地裂の必殺": "earth",
    u"乱気の必殺": "wind",
    u"天光の必殺": "light",
    u"奈落の必殺": "dark"
}

skillnamelist["normalHissatsuM"] = {
    u"業火の必殺": "fire",
    u"渦潮の必殺": "water",
    u"大地の必殺": "earth",
    u"竜巻の必殺": "wind",
    u"雷電の必殺": "light",
    u"憎悪の必殺": "dark"
}

skillnamelist["normalEiketsuL"] = {
    u"紅蓮の英傑": "fire",
    u"霧氷の英傑": "water",
    u"地裂の英傑": "earth",
    u"乱気の英傑": "wind",
    u"天光の英傑": "light",
    u"奈落の英傑": "dark"
}

skillnamelist["normalBoukunLLL"] = {
    u"紅蓮の暴君II": "fire",
    u"霧氷の暴君II": "water",
    u"地裂の暴君II": "earth",
    u"乱気の暴君II": "wind",
    u"天光の暴君II": "light",
    u"奈落の暴君II": "dark"
}

skillnamelist["normalBoukunL"] = {
    u"紅蓮の暴君": "fire",
    u"霧氷の暴君": "water",
    u"地裂の暴君": "earth",
    u"乱気の暴君": "wind",
    u"天光の暴君": "light",
    u"奈落の暴君": "dark"
}

skillnamelist["normalRasetsuM"] = {
    u"業火の羅刹": "fire",
    u"渦潮の羅刹": "water",
    u"大地の羅刹": "earth",
    u"竜巻の羅刹": "wind",
    u"雷電の羅刹": "light",
    u"憎悪の羅刹": "dark"
}

# Essence
skillnamelist["normalSeisyouM"] = {
    u"業火の星晶": "fire",
    u"渦潮の星晶": "water",
    u"大地の星晶": "earth",
    u"竜巻の星晶": "wind",
    u"雷電の星晶": "light",
    u"憎悪の星晶": "dark"
}

skillnamelist["normalElementL"] = {
    u"紅蓮の進境": "fire",
    u"霧氷の進境": "water",
    u"地裂の進境": "earth",
    u"乱気の進境": "wind",
    u"天光の進境": "light",
    u"奈落の進境": "dark"
}

skillnamelist["normalElementM"] = {
    u"業火の進境": "fire",
    u"渦潮の進境": "water",
    u"大地の進境": "earth",
    u"竜巻の進境": "wind",
    u"雷電の進境": "light",
    u"憎悪の進境": "dark",
}

skillnamelist["normalSoka"] = {
    u"竜巻の楚歌": "wind",
}

skillnamelist["rankiShikku"] = {u"乱気の疾駆・壱": "wind"}
skillnamelist["gurenJuin"] = {u"紅蓮の呪印・弐": "fire"}
skillnamelist["chiretsuSenwaku"] = {u"地裂の煽惑・参": "earth"}
skillnamelist["muhyoTuiga"] = {u"霧氷の追牙・肆": "water"}

skillnamelist["normalHaisuiLL"] = {
    u"炎威の背水": "fire"
}

skillnamelist["normalCriticalLLL"] = {
    u"水禍の技巧": "water"
}

skillnamelist["normalHiouLL"] = {
    u"巌迫の秘奥": "earth"
}

skillnamelist["normalLLLL"] = {
    u"劫風の攻刃": "wind",
}

skillnamelist["normalSanteLL"] = {
    u"威光の三手": "light",
}

skillnamelist["normalKonshinLLL"] = {
    u"呪蝕の渾身": "dark"
}

# Magna Skills / 方陣スキル #################################################################################################

# Might II / 攻刃II
skillnamelist["magnaL"] = {
    u"機炎方陣・攻刃II": "fire",
    u"海神方陣・攻刃II": "water",
    u"創樹方陣・攻刃II": "earth",
    u"嵐竜方陣・攻刃II": "wind",
    u"騎解方陣・攻刃II": "light",
    u"黒霧方陣・攻刃II": "dark"
}

# Might / 攻刃(中)
skillnamelist["magnaM"] = {
    u"機炎方陣・攻刃": "fire",
    u"海神方陣・攻刃": "water",
    u"創樹方陣・攻刃": "earth",
    u"嵐竜方陣・攻刃": "wind",
    u"騎解方陣・攻刃": "light",
    u"黒霧方陣・攻刃": "dark"
}

# Aegis II / 守護II
skillnamelist["magnaHPL"] = {
    u"機炎方陣・守護II": "fire",
    u"海神方陣・守護II": "water",
    u"創樹方陣・守護II": "earth",
    u"嵐竜方陣・守護II": "wind",
    u"騎解方陣・守護II": "light",
    u"黒霧方陣・守護II": "dark"
}

# Aegis / 守護(中)
skillnamelist["magnaHPM"] = {
    u"機炎方陣・守護": "fire",
    u"海神方陣・守護": "water",
    u"創樹方陣・守護": "earth",
    u"嵐竜方陣・守護": "wind",
    u"騎解方陣・守護": "light",
    u"黒霧方陣・守護": "dark"
}

# Aegis / 守護(小)
skillnamelist["magnaHPS"] = {
    u"機炎方陣・守護\(小\)": "fire",
    u"海神方陣・守護\(小\)": "water",
    u"創樹方陣・守護\(小\)": "earth",
    u"嵐竜方陣・守護\(小\)": "wind",
    u"騎解方陣・守護\(小\)": "light",
    u"黒霧方陣・守護\(小\)": "dark"
}

# Dual-Edge / 二手(中)
skillnamelist["magnaNiteM"] = {
    u"機炎方陣・二手": "fire",
    u"海神方陣・二手": "water",
    u"創樹方陣・二手": "earth",
    u"嵐竜方陣・二手": "wind",
    u"騎解方陣・二手": "light",
    u"黒霧方陣・二手": "dark"
}

# Devastation / 破壊(小)
skillnamelist["magnaHakaiS"] = {
    u"機炎方陣・破壊": "fire",
    u"海神方陣・破壊": "water",
    u"創樹方陣・破壊": "earth",
    u"嵐竜方陣・破壊": "wind",
    u"騎解方陣・破壊": "light",
    u"黒霧方陣・破壊": "dark"
}

# Verity II / 技巧II
skillnamelist["magnaCriticalL"] = {
    u"機炎方陣・技巧II": "fire",
    u"海神方陣・技巧II": "water",
    u"創樹方陣・技巧II": "earth",
    u"嵐竜方陣・技巧II": "wind",
    u"騎解方陣・技巧II": "light",
    u"黒霧方陣・技巧II": "dark"
}

# Enmity III / 背水III
skillnamelist["magnaHaisuiL"] = {
    u"機炎方陣・背水III": "fire",
    u"海神方陣・背水III": "water",
    u"創樹方陣・背水III": "earth",
    u"嵐竜方陣・背水III": "wind",
    u"騎解方陣・背水III": "light",
    u"黒霧方陣・背水III": "dark"
}

# Enmity II / 背水II
skillnamelist["magnaHaisuiM"] = {
    u"機炎方陣・背水II": "fire",
    u"海神方陣・背水II": "water",
    u"創樹方陣・背水II": "earth",
    u"嵐竜方陣・背水II": "wind",
    u"騎解方陣・背水II": "light",
    u"黒霧方陣・背水II": "dark"
}

# Enmity / 背水(小)
skillnamelist["magnaHaisuiS"] = {
    u"機炎方陣・背水": "fire",
    u"海神方陣・背水": "water",
    u"創樹方陣・背水": "earth",
    u"嵐竜方陣・背水": "wind",
    u"騎解方陣・背水": "light",
    u"黒霧方陣・背水": "dark"
}

# Stamina II / 渾身II
skillnamelist["magnaKonshinL"] = {
    u"機炎方陣・渾身II": "fire",
    u"海神方陣・渾身II": "water",
    u"創樹方陣・渾身II": "earth",
    u"嵐竜方陣・渾身II": "wind",
    u"騎解方陣・渾身II": "light",
    u"黒霧方陣・渾身II": "dark"
}

# Stamina / 渾身(中)
skillnamelist["magnaKonshinM"] = {
    u"機炎方陣・渾身": "fire",
    u"海神方陣・渾身": "water",
    u"創樹方陣・渾身": "earth",
    u"嵐竜方陣・渾身": "wind",
    u"騎解方陣・渾身": "light",
    u"黒霧方陣・渾身": "dark"
}

# 攻刃 + 守護
skillnamelist["magnaKamuiL"] = {
    u"機炎方陣・神威III": "fire",
    u"海神方陣・神威III": "water",
    u"創樹方陣・神威III": "earth",
    u"嵐竜方陣・神威III": "wind",
    u"騎解方陣・神威III": "light",
    u"黒霧方陣・神威III": "dark"
}

skillnamelist["magnaKamuiM"] = {
    u"機炎方陣・神威II": "fire",
    u"海神方陣・神威II": "water",
    u"創樹方陣・神威II": "earth",
    u"嵐竜方陣・神威II": "wind",
    u"騎解方陣・神威II": "light",
    u"黒霧方陣・神威II": "dark"
}

skillnamelist["magnaKamui"] = {
    u"機炎方陣・神威": "fire",
    u"海神方陣・神威": "water",
    u"創樹方陣・神威": "earth",
    u"嵐竜方陣・神威": "wind",
    u"騎解方陣・神威": "light",
    u"黒霧方陣・神威": "dark"
}

# 攻刃 + 二手
skillnamelist["magnaMusouM"] = {
    u"機炎方陣・無双": "fire",
    u"海神方陣・無双": "water",
    u"創樹方陣・無双": "earth",
    u"嵐竜方陣・無双": "wind",
    u"騎解方陣・無双": "light",
    u"黒霧方陣・無双": "dark"
}

# 攻刃 + 破壊
skillnamelist["magnaRanbuM"] = {
    u"機炎方陣・乱舞": "fire",
    u"海神方陣・乱舞": "water",
    u"創樹方陣・乱舞": "earth",
    u"嵐竜方陣・乱舞": "wind",
    u"騎解方陣・乱舞": "light",
    u"黒霧方陣・乱舞": "dark"
}

# 攻刃 + 技巧
skillnamelist["magnaSetsuna"] = {
    u"機炎方陣・刹那II": "fire",
    u"海神方陣・刹那II": "water",
    u"創樹方陣・刹那II": "earth",
    u"嵐竜方陣・刹那II": "wind",
    u"騎解方陣・刹那II": "light",
    u"黒霧方陣・刹那II": "dark"
}

skillnamelist["magnaSetsunaS"] = {
    u"機炎方陣・刹那": "fire",
    u"海神方陣・刹那": "water",
    u"創樹方陣・刹那": "earth",
    u"嵐竜方陣・刹那": "wind",
    u"騎解方陣・刹那": "light",
    u"黒霧方陣・刹那": "dark"
}

# 守護 + 二手
# Medium hp up + double atk rate up
skillnamelist["magnaGunshinM"] = {
    u"機炎方陣・軍神II": "fire",
    u"海神方陣・軍神II": "water",
    u"創樹方陣・軍神II": "earth",
    u"嵐竜方陣・軍神II": "wind",
    u"騎解方陣・軍神II": "light",
    u"黒霧方陣・軍神II": "dark"
}

# Small hp up + double atk rate up
skillnamelist["magnaGunshinS"] = {
    u"機炎方陣・軍神": "fire",
    u"海神方陣・軍神": "water",
    u"創樹方陣・軍神": "earth",
    u"嵐竜方陣・軍神": "wind",
    u"騎解方陣・軍神": "light",
    u"黒霧方陣・軍神": "dark"
}

# 守護 + 見切
skillnamelist["magnaFukashinS"] = {
    u"機炎方陣・不可侵": "fire",
    u"海神方陣・不可侵": "water",
    u"創樹方陣・不可侵": "earth",
    u"嵐竜方陣・不可侵": "wind",
    u"騎解方陣・不可侵": "light",
    u"黒霧方陣・不可侵": "dark"
}

# 二手 + 破壊
skillnamelist["magnaSanteL"] = {
    u"機炎方陣・三手": "fire",
    u"海神方陣・三手": "water",
    u"創樹方陣・三手": "earth",
    u"嵐竜方陣・三手": "wind",
    u"騎解方陣・三手": "light",
    u"黒霧方陣・三手": "dark"
}

# 二手 + 技巧
skillnamelist["magnaKatsumiM"] = {
    u"機炎方陣・克己": "fire",
    u"海神方陣・克己": "water",
    u"創樹方陣・克己": "earth",
    u"嵐竜方陣・克己": "wind",
    u"騎解方陣・克己": "light",
    u"黒霧方陣・克己": "dark"
}

# 二手 + 見切
skillnamelist["magnaKatsumokuS"] = {
    u"機炎方陣・括目": "fire",
    u"海神方陣・括目": "water",
    u"創樹方陣・括目": "earth",
    u"嵐竜方陣・括目": "wind",
    u"騎解方陣・括目": "light",
    u"黒霧方陣・括目": "dark"
}

# 技巧 + 見切
# Critical skill (M)
skillnamelist["magnaCriticalM"] = {
    u"機炎方陣・意志": "fire",
    u"海神方陣・意志": "water",
    u"創樹方陣・意志": "earth",
    u"嵐竜方陣・意志": "wind",
    u"騎解方陣・意志": "light",
    u"黒霧方陣・意志": "dark"
}

# 秘奥 + (奥義上限上昇)
skillnamelist["magnaHissatsuM"] = {
    u"機炎方陣・必殺": "fire",
    u"海神方陣・必殺": "water",
    u"創樹方陣・必殺": "earth",
    u"嵐竜方陣・必殺": "wind",
    u"騎解方陣・必殺": "light",
    u"黒霧方陣・必殺": "dark"
}

# 攻刃 + (HP-10%)
skillnamelist["magnaBoukun"] = {
    u"機炎方陣・暴君": "fire",
    u"海神方陣・暴君": "water",
    u"創樹方陣・暴君": "earth",
    u"嵐竜方陣・暴君": "wind",
    u"騎解方陣・暴君": "light",
    u"黒霧方陣・暴君": "dark"
}

# 攻刃 + (DA確率-10%)
skillnamelist["magnaRasetsuM"] = {
    u"機炎方陣・羅刹": "fire",
    u"海神方陣・羅刹": "water",
    u"創樹方陣・羅刹": "earth",
    u"嵐竜方陣・羅刹": "wind",
    u"騎解方陣・羅刹": "light",
    u"黒霧方陣・羅刹": "dark"
}

# (得意武器が「杖」のキャラの) 攻刃
skillnamelist["magnaJojutsuL"] = {
    u"機炎方陣・杖術": "fire",
    u"海神方陣・杖術": "water",
    u"創樹方陣・杖術": "earth",
    u"嵐竜方陣・杖術": "wind",
    u"騎解方陣・杖術": "light",
    u"黒霧方陣・杖術": "dark"
}

# (得意武器が「格闘」のキャラの) 攻刃
skillnamelist["magnaKenbuL"] = {
    u"機炎方陣・拳武": "fire",
    u"海神方陣・拳武": "water",
    u"創樹方陣・拳武": "earth",
    u"嵐竜方陣・拳武": "wind",
    u"騎解方陣・拳武": "light",
    u"黒霧方陣・拳武": "dark"
}

# (種族が「星晶獣」のキャラの) 攻刃
skillnamelist["magnaSeisyouM"] = {
    u"機炎方陣・星晶": "fire",
    u"海神方陣・星晶": "water",
    u"創樹方陣・星晶": "earth",
    u"嵐竜方陣・星晶": "wind",
    u"騎解方陣・星晶": "light",
    u"黒霧方陣・星晶": "dark"
}

# 経過ターンに応じて〇属性キャラの〇属性攻撃力が上昇
skillnamelist["magnaElementM"] = {
    u"機炎方陣・進境II": "fire",
    u"海神方陣・進境II": "water",
    u"創樹方陣・進境II": "earth",
    u"嵐竜方陣・進境II": "wind",
}

# バトル開始時から8ターンの間攻撃力上昇
skillnamelist["magnaSoka"] = {
    u"嵐竜方陣・楚歌": "wind",
}

# EX Skills / EXスキル ####################################################################################################

# Unknown Skills / アンノウンスキル
skillnamelist["unknownL"] = {u"アンノウン・ATK II": "unknown"}
skillnamelist["unknownM"] = {u"アンノウン・ATK": "unknown"}
skillnamelist["unknownHPL"] = {u"アンノウン・VIT II": "unknown"}
skillnamelist["unknownHPM"] = {u"アンノウン・VIT": "unknown"}

# EX攻刃(大)
skillnamelist["strengthL"] = {
    u"蒼薔薇の棘": "water",
    u"翠薔薇の棘": "wind",
    u"橙薔薇の棘": "earth",
    u"紅薔薇の棘": "fire",
    u"震天の雷鳴": "light",
    u"靂天の暗雲": "dark",
    u"ブレイズオブアームズ": "fire",
    u"フラッドオブアームズ": "water",
    u"グラウンドオブアームズ": "earth",
    u"ゲイルオブアームズ": "wind",
    u"シャインオブアームズ": "light",
    u"シャドウオブアームズ": "dark",
    u"ストレングス": "unknown",
    u"セービングアタック": "water",
    u"烈光の至恩": "dark",
    u"自動辻斬装置": "water",
    u"Vスキル": "earth",
    u"その魂よ、安らかに": "light",
    u"炎の背骨": "fire",
    u"西風のラプソディ": "wind",
    u"ポイント・オブ・エイム": "earth",
    u"我流の太刀筋": "wind",
    u"カースドテンタクル": "dark",
    u"森林の祝福": "wind",
    u"お友達になってくれる？": "dark",
    u"天の福音": "light",
    u"貴方へ贈る言葉": "wind",
    u"大いなる業": "light",
    u"ロイヤルアフェクション": "earth",
    u"超カッコいい攻刃": "water",
    u"叉棘": "fire",
    u"マナリアの聖なる息吹": "wind",
    u"天下五剣": "light",
    u"利無動": "water",
    u"紫水の光輝": "dark",
    u"闇の力を秘めし鍵": "dark",
    u"狐火の閃揺": "fire",
    u"竜伐の心得": "earth",
    u"肉削ぐ撓刃": "wind",
    u"アーキテクト・ATK II": "dark",
    u"菩提の探究": "wind",
    u"天の理": "light",
    u"超壊獣デスパワーZ": "dark",
    u"阿笠博士の発明品": "light",
    u"ウィーバースタンス": "wind",
    u"サウザンド・ドリーム": "fire",
    u"極上バナナ": "water",
    u"ザ・ファントム": "dark",
    u"フォルテ・スオーノ": "earth",
    u"頂点捕食者": "light",
    u"サンシャイナー": "water",
    u"スクールフレンズ": "fire",
    u"摩武駄致": "wind",
    u"螺旋の攻刃": "earth",
    u"プリズムストーンの力": "light",
    u"テイスティーズグッド": "fire",
    u"紅ニ染マル刃": "dark",
    u"フローズン・ブレード": "water",
    u"ジャスティス・ロッド": "light",
    u"トラフィックエナジー": "light",
    u"ふわふわしっぽ": "earth",
    u"獅子と牛の咆哮": "dark",
    u"サイコ攻刃": "earth",
    u"退路無き攻刃": "water",
    u"パワーボム": "earth",
    u"デヴァイサー": "wind",
    u"シャークアタック！": "dark",
    u"産地直送の攻刃": "water",
    u"スクールアイドル": "wind",
    u"ワン・ライト": "light",
    u"殺戮の女神": "wind",
    u"破竜の攻刃": "earth",
    u"残る霞火、あへなし": "light",
    u"暴風の残滓": "wind",
    u"ガチャピンの攻刃": "wind",
    u"あふれだす旨味の攻刃": "earth",
    u"資材切断の攻刃": "dark",
    u"六波羅蜜の攻刃": "dark",
    u"プロフェッショナルツール": "earth",
    u"猛将の攻刃": "fire",
    u"エレクトリックな攻刃": "wind",
    u"開封の攻刃": "water",
    u"リゾートの攻刃": "light",
    u"英霊の攻刃": "fire",
    u"シャドバプレイヤー": "fire",
    u"護国の攻刃": "dark",
    u"錬成の攻刃": "earth",
    u"戦女の攻刃": "wind",
    u"普及型壊天刃": "light",
    u"竹の攻刃": "earth",
    u"衛星の攻刃": "dark",
    u"美花の攻刃": "fire",
    u"光矢の攻刃": "light",
    u"本気の攻刃": "earth",
    u"白樺の攻刃": "wind",
    u"２度あることは３度ある": "light",
    u"くうきの塊": "water",
    u"命宿りし模造の槍": "earth",
    u"南海の魔神からの戦利品": "earth",
}

# EX攻刃(中)
skillnamelist["strengthM"] = {
    u"ブレイズオブネイルズ": "fire",
    u"フラッドオブネイルズ": "water",
    u"グラウンドオブネイルズ": "earth",
    u"ゲイルオブネイルズ": "wind",
    u"シャインオブネイルズ": "light",
    u"シャドウオブネイルズ": "dark",
    u"大自然の摂理": "light",
    u"花戦の攻刃": "wind",
    u"錬金の攻刃": "light",
    u"美食の攻刃": "earth",
    u"刺々の攻刃": "fire",
    u"マナリアの攻刃": "wind",
    u"土方の愛刀": "fire",
    u"国広第一の傑作": "earth",
    u"龍馬の愛刀": "wind",
    u"足利宝剣": "dark",
    u"紫水の攻刃": "dark",
    u"狐火の攻刃": "fire",
    u"竜伐の攻刃": "earth",
    u"アーキテクト・ATK": "dark",
    u"煩悩の攻刃": "wind",
    u"座天の攻刃": "light",
    u"壊獣デスパワーX": "dark",
    u"熱砂の攻刃": "fire",
    u"芳醇バナナ": "water",
    u"音階の攻刃": "earth",
    u"新鮮で旬な攻刃": "light",
    u"特攻の攻刃": "wind",
    u"穿孔の攻刃": "unknown",
    u"デリシャスな攻刃": "fire",
    u"恨ミノ攻刃": "dark",
    u"ATKシール": "light",
    u"にくきゅうの攻刃": "earth",
    u"黒い残滓の攻刃": "dark",
    u"白い残滓の攻刃": "light",
    u"ゴリラの攻刃": "earth",
    u"つはものの攻刃": "water",
    u"稽古の攻刃": "earth",
    u"鮫肌の攻刃": "dark",
    u"倒れずの攻刃": "water",
    u"特攻の攻刃": "wind",
    u"勇武の攻刃": "wind",
    u"黒竜騎士団の攻刃": "earth",
    u"燐火の攻刃": "light",
    u"下降気流の攻刃": "wind",
    u"返しの達人": "earth",
    u"裏社会の攻刃": "light",
    u"手練れの攻刃": "earth",
    u"雑兵の攻刃": "fire",
    u"荒磯の攻刃": "light",
    u"貴金の攻刃": "earth",
    u"戦狂の攻刃": "wind",
    u"圧縮空気の攻刃": "light",
    u"柴刈りの攻刃": "earth",
    u"白兵戦用制御の攻刃": "dark",
    u"鳳梨の攻刃": "fire",
    u"躾長の攻刃": "earth",
}

# EX攻刃(小)
skillnamelist["strengthS"] = {
    u"スピードスペル": "light",
}

# EX守護(大) 工事中
# skillnamelist[""] = {
#     u"ブレイズオブタフネス": "fire",
#     u"フラッドオブタフネス": "water",
#     u"グラウンドオブタフネス": "earth",
#     u"ゲイルオブタフネス": "wind",
#     u"シャインオブタフネス": "light",
#     u"シャドウオブタフネス": "dark",
#     u"ゴールドスライムの守護": "light"
#     u"シルバースライムの守護": "dark",
# }

# EX守護(中) 工事中
# skillnamelist[""] = {
#     u"花戦の守護": "wind",
#     u"錬金の守護": "light",
#     u"美食の守護": "earth",
#     u"スタイリッシュな守護": "water",
#     u"刺々の守護": "fire",
#     u"マナリアの守護": "wind",
#     u"紫水の守護": "dark",
#     u"狐火の守護": "fire",
#     u"竜伐の守護": "earth",
#     u"アーキテクト・VIT": "dark",
#     u"煩悩の守護": "wind",
#     u"智天の守護": "light",
#     u"壊獣デスパワーQ": "dark",
#     u"熱砂の守護": "fire",
#     u"甘熟バナナ": "water",
#     u"音階の守護": "earth",
#     u"香ばしい香りの守護": "light",
#     u"特攻の守護": "wind",
#     u"穿孔の守護": "earth",
#     u"デリシャスな守護": "fire",
#     u"恨ミノ守護": "dark",
#     u"VITシール": "light",
#     u"にくきゅうの守護": "earth",
#     u"スケバンの守護": "earth",
#     u"つはものの守護": "water",
#     u"稽古の守護": "earth",
#     u"鮫肌の守護": "dark",
#     u"抜きわれの守護": "water",
#     u"理知の守護": "wind",
#     u"黒竜騎士団の守護": "earth",
#     u"燐火の守護": "light",
#     u"上昇気流の守護": "wind",
#     u"食べ歩きの守護": "earth",
#     u"緋緋色の守護": "dark",
#     u"裏社会の守護": "dark",
#     u"手練れの守護": "earth",
#     u"心配りの守護": "wind",
#     u"二枚貝の守護": "water",
#     u"紋旗の守護": "fire",
#     u"奮戦の守護": "dark",
#     u"骨格の守護": "light",
#     u"サウナーの守護": "wind",
#     u"スライムの守護": "water",
# }

skillnamelist["exATKandHPM"] = {
    u"蒼薔薇の髄": "water",
    u"翠薔薇の髄": "wind",
    u"橙薔薇の髄": "earth",
    u"紅薔薇の髄": "fire",
}

skillnamelist["strengthLL"] = {
    u"灼滅の覇道": "fire",
    u"裁考の覇道": "earth",
    u"人馬の覇道": "wind",
    u"氷逆の覇道": "water",
    u"幻魔の覇道": "dark",
    u"妃光の覇道": "light"
}

skillnamelist["strengthLLL"] = {
    u"紅炎の支配者": "fire",
    u"氷霜の支配者": "water",
    u"花樹の支配者": "earth",
    u"嵐翠の支配者": "wind",
    u"白輝の支配者": "light",
    u"禍滅の支配者": "dark"
}

skillnamelist["strengthLLandHPS"] = {
    u"真・灼滅の覇道": "fire",
    u"真・裁考の覇道": "earth",
    u"真・人馬の覇道": "wind",
    u"真・氷逆の覇道": "water",
    u"真・幻魔の覇道": "dark",
    u"真・妃光の覇道": "light"
}

skillnamelist["exSensei"] = {
    u"封印されし未確認の力": "dark",
}

skillnamelist["dracoATK"] = {
    u"ウィルナスの炎威": "fire",
    u"ワムデュスの水禍": "water",
    u"ガレヲンの巌迫": "earth",
    u"イーウィヤの劫風": "wind",
    u"ル・オーの威光": "light",
    u"フェディエルの呪蝕": "dark"
}

skillnamelist["strengthHaisuiM"] = {u"マジックチャージ": "light"}
skillnamelist["unknownOtherBoukunL"] = {u"ミフネ流剣法・極意": "fire", u"インテリジェンス": "dark"}
skillnamelist["unknownOtherNiteS"] = {u"ミフネ流剣法・双星": "fire", u"デクステリティ": "dark"}

# 特殊武器 #################################################################################################################

# Seraphic Weapons / セラフィックウェポン
skillnamelist["tenshiShukufukuIII"] = {
    u"ミカエルの祝福III": "fire",
    u"ガブリエルの祝福III": "water",
    u"ウリエルの祝福III": "earth",
    u"ラファエルの祝福III": "wind",
    u"双子天司の導きIII": "light",
    u"堕落のすゝめIII": "dark",
}

skillnamelist["tenshiShukufukuII"] = {
    u"ミカエルの祝福II": "fire",
    u"ガブリエルの祝福II": "water",
    u"ウリエルの祝福II": "earth",
    u"ラファエルの祝福II": "wind",
    u"双子天司の導きII": "light",
    u"堕落のすゝめII": "dark",
}

skillnamelist["tenshiShukufuku"] = {
    u"ミカエルの祝福": "fire",
    u"ガブリエルの祝福": "water",
    u"ウリエルの祝福": "earth",
    u"ラファエルの祝福": "wind",
    u"双子天司の導き": "light",
    u"堕落のすゝめ": "dark"
}

# Hollowsky Weapons / 虚ろなる神器
skillnamelist["akasha-sword"] = {u"虚脱の隻翼": "dark"}
skillnamelist["akasha-spear"] = {u"虚栄の矛戟": "fire"}
skillnamelist["akasha-axe"] = {u"虚勢の巌": "earth"}
skillnamelist["akasha-wand"] = {u"虚飾の隻腕": "water"}
skillnamelist["akasha-bow"] = {u"虚像の鋒鏑": "light"}
#Covenant
skillnamelist["impervious-covenant"] = {u"不壊の誓約": "fire"}
skillnamelist["victorious-covenant"] = {u"凱歌の誓約": "water"}
skillnamelist["contentious-covenant"] = {u"修羅の誓約": "earth"}
skillnamelist["deleterious-covenant"] = {u"致命の誓約": "light"}
skillnamelist["calamitous-covenant"] = {u"災禍の誓約": "dark"}

# Astral Weapons / アストラルウェポン
skillnamelist["astralblow"] = {
    u"アストラル・ブロー": "fire"
}
skillnamelist["astralthrust"] = {
    u"アストラル・スラスト": "water"
}
skillnamelist["astralecho"] = {
    u"アストラル・エコー": "wind"
}
skillnamelist["astralclaw"] = {
    u"アストラル・クロー": "dark"
}

# Ultima Weapons / オメガウェポン
# Attribute as a temporary fire
skillnamelist["omega-raw"] = {
    u"グラディウス・ルーベル": "fire",
    u"シーカー・ルーベル": "fire",
    u"ランセア・ルーベル": "fire",
    u"ラブリュス・ルーベル": "fire",
    u"バクラム・ルーベル": "fire",
    u"アルマ・ルーベル": "fire",
    u"ルクトール・ルーベル": "fire",
    u"アルクス・ルーベル": "fire",
    u"ムーシカ・ルーベル": "fire",
    u"マカエラ・ルーベル": "fire",
}

# Bahamut Weapons / バハムートウェポン
# Bahamut fist has the same skill name so process first
skillnamelist["bahaFUHP-fist"] = {u"ヒュムアニムス・メンスII": "dark"}
skillnamelist["bahaFUHP-katana"] = {u"ドーラアニムス・メンスII": "dark"}
skillnamelist["bahaFUHP-bow"] = {u"エルンアニムス・メンスII": "dark"}
skillnamelist["bahaFUHP-music"] = {u"ハヴンアニムス・メンスII": "dark"}
skillnamelist["bahaAT-dagger"] = {u"ヒュムアニムス・ウィス": "dark"}
skillnamelist["bahaAT-axe"] = {u"ドーラアニムス・ウィス": "dark"}
skillnamelist["bahaAT-spear"] = {u"エルンアニムス・ウィス": "dark"}
skillnamelist["bahaAT-gun"] = {u"ハヴンアニムス・ウィス": "dark"}
skillnamelist["bahaATHP-sword"] = {u"コンキリオ・ルーベル": "dark"}
skillnamelist["bahaATHP-wand"] = {u"コンキリオ・ケルレウス": "dark"}
skillnamelist["bahaHP-fist"] = {u"ヒュムアニムス・メンス": "dark"}
skillnamelist["bahaHP-katana"] = {u"ドーラアニムス・メンス": "dark"}
skillnamelist["bahaHP-bow"] = {u"エルンアニムス・メンス": "dark"}
skillnamelist["bahaHP-music"] = {u"ハヴンアニムス・メンス": "dark"}
skillnamelist["bahaFUATHP-sword"] = {u"コンキリオ・イグニス": "dark"}
skillnamelist["bahaFUATHP-dagger"] = {u"コンキリオ・ウェントス": "dark"}
skillnamelist["bahaFUATHP-spear"] = {u"コンキリオ・コルヌ": "dark"}
skillnamelist["bahaFUATHP-axe"] = {u"コンキリオ・テラ": "dark"}
skillnamelist["bahaFUATHP-wand"] = {u"コンキリオ・インベル": "dark"}
skillnamelist["bahaFUATHP-gun"] = {u"コンキリオ・アルボス": "dark"}
# skillnamelist[""] = {u"ヴィータ・イグニス": "dark"}
# skillnamelist[""] = {u"インクルシオー・ウェントス": "dark"}
# skillnamelist[""] = {u"インクルシオー・コルヌ": "dark"}
# skillnamelist[""] = {u"インクルシオー・テラ": "dark"}
# skillnamelist[""] = {u"ヴィータ・インベル": "dark"}
# skillnamelist[""] = {u"インクルシオー・アルボス": "dark"}
# skillnamelist[""] = {u"ラピドゥス・ヒュムアニムス": "dark"}
# skillnamelist[""] = {u"ラピドゥス・エルンアニムス": "dark"}
# skillnamelist[""] = {u"ラピドゥス・ハヴンアニムス": "dark"}
# skillnamelist[""] = {u"ラピドゥス・ドーラアニムス": "dark"}

# Cosmos Weapons / コスモスシリーズ
skillnamelist["cosmos-swordII"] = {u"ソード・オブ・コスモスII": "light"}
skillnamelist["cosmos-daggerII"] = {u"ダガー・オブ・コスモスII": "light"}
skillnamelist["cosmos-spearII"] = {u"ランス・オブ・コスモスII": "light"}
skillnamelist["cosmos-axeII"] = {u"サイス・オブ・コスモスII": "light"}
skillnamelist["cosmos-wandII"] = {u"ロッド・オブ・コスモスII": "light"}
skillnamelist["cosmos-gunII"] = {u"ガン・オブ・コスモスII": "light"}
skillnamelist["cosmos-fistII"] = {u"ガントレット・オブ・コスモスII": "light"}
skillnamelist["cosmos-bowII"] = {u"アロー・オブ・コスモスII": "light"}
skillnamelist["cosmos-musicII"] = {u"ハープ・オブ・コスモスII": "light"}
skillnamelist["cosmos-katanaII"] = {u"ブレイド・オブ・コスモスII": "light"}
skillnamelist["cosmos-sword"] = {u"ソード・オブ・コスモス": "light"}
skillnamelist["cosmos-dagger"] = {u"ダガー・オブ・コスモス": "light"}
skillnamelist["cosmos-spear"] = {u"ランス・オブ・コスモス": "light"}
skillnamelist["cosmos-axe"] = {u"サイス・オブ・コスモス": "light"}
skillnamelist["cosmos-wand"] = {u"ロッド・オブ・コスモス": "light"}
skillnamelist["cosmos-gun"] = {u"ガン・オブ・コスモス": "light"}
skillnamelist["cosmos-fist"] = {u"ガントレット・オブ・コスモス": "light"}
skillnamelist["cosmos-bow"] = {u"アロー・オブ・コスモス": "light"}
skillnamelist["cosmos-music"] = {u"ハープ・オブ・コスモス": "light"}
skillnamelist["cosmos-katana"] = {u"ブレイド・オブ・コスモス": "light"}
skillnamelist["cosmos-sword-limit"] = {u"秩序の蒼剣": "light"}
skillnamelist["cosmos-dagger-limit"] = {u"秩序の蒼刃": "light"}
skillnamelist["cosmos-spear-limit"] = {u"秩序の蒼槍": "light"}
skillnamelist["cosmos-axe-limit"] = {u"秩序の蒼鎌": "light"}
skillnamelist["cosmos-wand-limit"] = {u"秩序の蒼杖": "light"}
skillnamelist["cosmos-gun-limit"] = {u"秩序の蒼銃": "light"}
skillnamelist["cosmos-fist-limit"] = {u"秩序の蒼拳": "light"}
skillnamelist["cosmos-bow-limit"] = {u"秩序の蒼弓": "light"}
skillnamelist["cosmos-music-limit"] = {u"秩序の蒼琴": "light"}
skillnamelist["cosmos-katana-limit"] = {u"秩序の蒼刀": "light"}

# Superlative Weapons / スペリオルシリーズ
# Attribute as a temporary all
skillnamelist["rightway_pathfinderII"] = {u"王道を征く者II": "all"}
skillnamelist["rightway_pathfinder"] = {u"王道を征く者": "all"}
skillnamelist["victorys_promise"] = {u"必勝の誓い": "all"}
skillnamelist["one_sting_one_killII"] = {u"一刺一殺II": "all"}
skillnamelist["one_sting_one_kill"] = {u"一刺一殺": "all"}
skillnamelist["god_of_warII"] = {u"戦神の打擲II": "all"}
skillnamelist["god_of_war"] = {u"戦神の打擲": "all"}
skillnamelist["apocalyptic_powerII"] = {u"万物を砕く剛技II": "all"}
skillnamelist["apocalyptic_power"] = {u"万物を砕く剛技": "all"}
skillnamelist["slaysnakes_mythII"] = {u"戮蛇の神刀II": "all"}
skillnamelist["slaysnakes_myth"] = {u"戮蛇の神刀": "all"}

skillnamelist["cherubimKonshin"] = {
    u"鷲と人間の思慮": "dark"
}

skillnamelist["sunbladeKonshin"] = {
    u"道天の眩耀": "light"
}

skillnamelist["diaboliHaisui"] = {
    u"普天の呼び声": "dark"
}

skillnamelist["kaijinnoyogen"] = {
    u"海神の予言": "water"
}

skillnamelist["normalAtkFistPugilism"] = {
    u"古代の闘術": "earth",
}

# Huanglong katana, Dawn Rising
skillnamelist["shinTenNoInori"] = {
    u"震天の祈り": "light",
    u"サンライト・ブースト": "earth",
}

skillnamelist["sensei"] = {
    u"先制の炎刃": "fire",
    u"先制の氷刃": "water",
    u"先制の光刃": "light",
    u"先制の地刃": "earth",
    u"先制の風刃": "wind",
    u"先制の闇刃": "dark",
}

# Damage cap up
skillnamelist["normalDamageLimit7"] = {
    u"焔の真髄": "fire",
    u"雪の真髄": "water",
    u"界の真髄": "earth",
    u"凪の真髄": "wind",
    u"煌の真髄": "light",
    u"煉の真髄": "dark",
    u"炎熱の刀身": "fire",
    u"賢者の加護": "earth",
    u"英雄の体躯": "light",
}
skillnamelist["normalDamageLimit10"] = {
    u"靂天の極致": "dark",
}
skillnamelist["huanglongHissatsu"] = {
    u"震天の境界へと至りし者": "light",
}

skillnamelist["zwei-echo"] = {
    u"レッド・ブロウ": "fire",
    u"ブルー・ブロウ": "water",
    u"イエロー・ブロウ": "earth",
    u"グリーン・ブロウ": "wind",
    u"ライト・ブロウ": "light",
    u"パープル・ブロウ": "dark",
}

skillnamelist["ougiDamageLimitExceedM"] = {
    u"イクシード・ファイア": "fire",
    u"イクシード・ウォータ": "water",
    u"イクシード・アース": "earth",
    u"イクシード・ウィンド": "wind",
    u"イクシード・ライト": "light",
    u"イクシード・ダーク": "dark",
}

skillnamelist["chainForce"] = {
    u"チェインフォース": "dark",
}

# New epic weapons
skillnamelist["epic-grandEpic"] = {
    u"エピックブランド・ゲイン": "none",
}
skillnamelist["epic-staffResonance"] = {
    u"レゾナンス・スタッフ": "water",
}
skillnamelist["epic-heroicTale"] = {
    u"ヒロイック・テイル": "earth",
}
skillnamelist["epic-absoluteEquality"] = {
    u"ソール・イコーリティ": "dark",
}

# 工事中
# skillnamelist[""] = {u"ボルテージ・オブ・ソード": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ダガー": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・スピア": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・アックス": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・スタッフ": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ガン": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ガントレット": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ボウ": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ハープ": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ブレイド": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ソードII": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ダガーII": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・スピアII": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・アックスII": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・スタッフII": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ガンII": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ガントレットII": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ボウII": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ハープII": ""}
# skillnamelist[""] = {u"ボルテージ・オブ・ブレイドII": ""}

# 工事中
# skillnamelist[""] = {u"レイジ・オブ・ソード": ""}
# skillnamelist[""] = {u"レイジ・オブ・ダガー": ""}
# skillnamelist[""] = {u"レイジ・オブ・スピア": ""}
# skillnamelist[""] = {u"レイジ・オブ・アックス": ""}
# skillnamelist[""] = {u"レイジ・オブ・スタッフ": ""}
# skillnamelist[""] = {u"レイジ・オブ・ガン": ""}
# skillnamelist[""] = {u"レイジ・オブ・ガントレット": ""}
# skillnamelist[""] = {u"レイジ・オブ・ボウ": ""}
# skillnamelist[""] = {u"レイジ・オブ・ハープ": ""}
# skillnamelist[""] = {u"レイジ・オブ・ブレイド": ""}

# 工事中
# skillnamelist[""] = {
#     u"スカーレット・ヴァイタリティー": "fire",
#     u"コバルト・ヴァイタリティー": "water",
#     u"アンバー・ヴァイタリティー": "earth",
#     u"ジェイド・ヴァイタリティー": "wind",
#     u"ゴールデン・ヴァイタリティー": "light",
#     u"グラファイト・ヴァイタリティー": "dark",
# }

# 工事中
# skillnamelist[""] = {
#     u"スカーレット・レゾネーター": "fire",
#     u"コバルト・レゾネーター": "water",
#     u"アンバー・レゾネーター": "earth",
#     u"ジェイド・レゾネーター": "wind",
#     u"ゴールデン・レゾネーター": "light",
#     u"グラファイト・レゾネーター": "dark",
# }

# Character specific weapon
skillnamelist["washiouKekkai"] = {u"鷲王の結界": "fire"}
skillnamelist["maihimeEnbu"] = {u"舞姫の演武": "water"}
skillnamelist["hengenKengi"] = {u"変幻自在の剣技": "dark"}
skillnamelist["kochoKenbu"] = {u"胡蝶の剣舞": "earth"}
skillnamelist["rigaiBishojo"] = {u"理外の美少女": "water"}
skillnamelist["normalHPL"][u"氷晶宮の加護"] = "water"
skillnamelist["normalL"][u"聖女の行進"] = "light"
skillnamelist["normalL"][u"天を統べる強風"] = "wind"
skillnamelist["normalL"][u"血啜りの一閃"] = "dark"
skillnamelist["normalL"][u"未完の錬金術"] = "fire"
skillnamelist["normalL"][u"英雄たる証明"] = "wind"
skillnamelist["normalL"][u"禁忌の悲恋"] = "dark"
skillnamelist["normalL"][u"狙撃の極意"] = "water"

# Other weapons that require adjustment
skillnamelist["extendedDjeetaNormalDATA30"] = {u"立体機動戦術": "wind"}
skillnamelist["one_night_party"] = {u"ワンナイ・パーリー": "none"}
skillnamelist["downfall_of_ignorance"] = {u"無明衰滅": "none"}
skillnamelist["succession_of_knighthood"] = {u"騎士の血脈": "none"}

# 工事中
# skillnamelist[""] = {
#     u'焔の約定': "fire",
#     u'雪の約定': "water",
#     u'界の約定': "earth",
#     u'凪の約定': "wind",
#     u'煌の約定': "light",
#     u'煉の約定': "dark",
# }

# 工事中
# skillnamelist[""] = {
#     u'焔の果断': "fire",
#     u'雪の果断': "water",
#     u'界の果断': "earth",
#     u'凪の果断': "wind",
#     u'煌の果断': "light",
#     u'煉の果断': "dark",
# }

skillnamelist["supplementalEmnity"] = {
    u"焔の剛毅": "fire",
    u"雪の剛毅": "water",
    u"界の剛毅": "earth",
    u"凪の剛毅": "wind",
    u"煌の剛毅": "light",
    u"煉の剛毅": "dark",
    u"朱の誓約": "fire",
}

skillnamelist["supplementalCritical"] = {
    u'碧の誓約': "water",
}

# 工事中
# skillnamelist[""] = {
#     u"スカーレット・クラフト": "fire",
#     u"コバルト・クラフト": "water",
#     u"アンバー・クラフト": "earth",
#     u"ジェイド・クラフト": "wind",
#     u"ゴールデン・クラフト": "light",
#     u"グラファイト・クラフト": "dark",
# }

skillnamelist["supplementalMulti"] = {
    u'白の誓約': "light",
}

# 工事中
# skillnamelist[""] = {
#     u'瑞風の誓約': "wind",
# }

skillnamelist["supplementalOugi"] = {
    u"焔の極意": "fire",
    u"雪の極意": "water",
    u"界の極意": "earth",
    u"凪の極意": "wind",
    u"煌の極意": "light",
    u"煉の極意": "dark",
    u"金の誓約": "earth",
}

skillnamelist["supplementalStaminaOugi"] = {
    u'焔の慈雨': "fire",
    u'雪の慈雨': "water",
    u'界の慈雨': "earth",
    u'凪の慈雨': "wind",
    u'煌の慈雨': "light",
    u'煉の慈雨': "dark",
    u'黒の誓約': "dark",
}

########################################################################################################################

armtypelist = OrderedDict()
armtypelist[u"剣"] = "sword"
armtypelist[u"銃"] = "gun"
armtypelist[u"短剣"] = "dagger"
armtypelist[u"槍"] = "spear"
armtypelist[u"斧"] = "axe"
armtypelist[u"杖"] = "wand"
armtypelist[u"格闘"] = "fist"
armtypelist[u"弓"] = "bow"
armtypelist[u"楽器"] = "music"
armtypelist[u"刀"] = "katana"

SERIES = {
    u"セラフィックウェポン": "seraphic",
    u"リミテッドシリーズ": "grand",
    u"終末の神器": "dark opus",
    u"ドラゴニックウェポン": "draconic",
    u"天星器": "revenant",
    u"十天光輝": "eternal splendor",
    u"プライマルシリーズ": "primal",
    u"四象武器": "beast",
    u"レガリアシリーズ": "regalia",
    u"マグナシリーズ": "omega",
    u"オールド・プライマルシリーズ": "olden primal",
    u"ミーレスシリーズ": "militis",
    u"虚ろなる神器": "hollowsky",
    u"六道武器": "xeno",
    u"アストラルウェポン": "astral",
    u"ローズシリーズ": "rose",
    u"オメガウェポン": "ultima",
    u"バハムートウェポン": "bahamut",
    u"エピックウェポン": "epic",
    u"エニアドシリーズ": "ennead",
    u"マリスシリーズ": "malice",
    u"メナスシリーズ": "menace",
    u"コスモスシリーズ": "cosmos",
    u"アンセスタルシリーズ": "ancestral",
    u"スペリオルシリーズ": "superlative",
    u"ヴィンテージシリーズ": "vintage",
    u"英雄武器": "class champion",
    u"複製品": "replicas",
    u"依代": "relics",
    u"朽ち果てた武器": "rusted",
    u"セフィリアン・オールドウェポン": "sephira",
    u"新世界の礎": "new world foundation",
    u"オイラは": "vyrmament",
    u"強化素材": "upgraders",
}

########################################################################################################################

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

# json translation
translation = json.load(open(os.path.join(path, "../txt_source/arm-translation.json"), "r", encoding="utf-8"))


def skill_replace(skill):
    for inner_skillname, onelist in skillnamelist.items():
        for skillname, element in onelist.items():
            if re.match(skillname, skill):
                return inner_skillname, element
    return "non", "none"


def type_replace(armtype):
    for armtypename, inner_armtype in armtypelist.items():
        if re.match(armtypename, armtype):
            return inner_armtype
    return "none"


def processCSVdata(csv_file_name, json_data, image_wiki_url_list, image_game_url_list, PROCESS_TYPE_SSR=True):
    key_pattern = re.compile("\d+")
    key_pattern = re.compile("(\w+\.png)")
    skill_pattern = re.compile("\[\[([\W\w]+)\>")
    jougen_4_pattern = re.compile(u"○")
    jougen_5_pattern = re.compile(u"◎")

    mycsv = csv.reader(open(csv_file_name, 'r', encoding="utf-8"), delimiter="|")

    for row in mycsv:
        newdict = OrderedDict()
        row_length = len(row)
        if row_length <= 1:
            continue

        # Row Lengths Overview
        #  8: 2nd + 3rd skills
        # 17: 3*
        # 19: 4*
        # 20: 4*
        # 21: 5*
        # 22: 5*
        has_3rd_skill: bool = row_length == 20 or row_length == 22
        row_iter = iter(row)
        for index, value in enumerate(row_iter):
            if index == 1:
                m = key_pattern.search(value)
                if m:
                    key = m.group(1)
            elif index == 2:
                name = value.replace("&br;", "")
                name = name.replace("[]", "")
                newdict["ja"] = name
            elif index == 3:
                # element
                if value.find("火") >= 0:
                    newdict["element"] = "fire"
                elif value.find("水") >= 0:
                    newdict["element"] = "water"
                elif value.find("土") >= 0:
                    newdict["element"] = "earth"
                elif value.find("風") >= 0:
                    newdict["element"] = "wind"
                elif value.find("光") >= 0:
                    newdict["element"] = "light"
                elif value.find("闇") >= 0:
                    newdict["element"] = "dark"
                elif value.find("全属性") >= 0:
                    newdict["element"] = "all"
                else:
                    newdict["element"] = "none"
            elif index == 4:
                # type
                newdict["type"] = type_replace(value)
            elif index == 7:
                skill = "non"
                element1 = "none"
                m = skill_pattern.search(value)
                if m:
                    skill, element1 = skill_replace(m.group(1))

                newdict["skill1"] = skill
            elif index == 8:
                # skill2
                skill2 = "non"
                element2 = "none"
                m = skill_pattern.search(value)
                if m:
                    skill2, element2 = skill_replace(m.group(1))

                if element2 == "none" or element2 == "unknown":
                    element2 = newdict["element"]

                newdict["skill2"] = skill2
                newdict["element2"] = element2

                # skill3
                skill3 = "non"
                element3 = "none"

                if has_3rd_skill:
                    # Read the next value without increment enumerate counter
                    value = next(row_iter)

                    m = skill_pattern.search(value)
                    if m:
                        skill3, element3 = skill_replace(m.group(1))

                if element3 == "none" or element3 == "unknown":
                    element3 = newdict["element"]

                newdict["skill3"] = skill3
                newdict["element3"] = element3

            elif index == 9:
                newdict["minhp"] = int(value)
            elif index == 10:
                newdict["minattack"] = int(value)
            elif index == 11:
                newdict["hp"] = int(value)
            elif index == 12:
                newdict["attack"] = int(value)
            elif index == 13:
                pass
            elif index == 14:
                newdict["series"] = SERIES.get(value, "none")
            elif index == 15:
                if PROCESS_TYPE_SSR:
                    if jougen_5_pattern.search(value):
                        newdict["slvmax"] = 20
                        newdict["maxlv"] = 200
                    elif jougen_4_pattern.search(value):
                        newdict["slvmax"] = 15
                        newdict["maxlv"] = 150
                    else:
                        newdict["slvmax"] = 10
                        newdict["maxlv"] = 100
                else:
                    if jougen_4_pattern.search(value):
                        newdict["slvmax"] = 15
                        newdict["maxlv"] = 120
                    else:
                        newdict["slvmax"] = 10
                        newdict["maxlv"] = 75
            elif index == 16 and newdict["slvmax"] >= 15:
                if PROCESS_TYPE_SSR:
                    newdict["hplv100"] = int(value)
                else:
                    newdict["hplv75"] = int(value)
            elif index == 17 and newdict["slvmax"] >= 15:
                if PROCESS_TYPE_SSR:
                    newdict["attacklv100"] = int(value)
                else:
                    newdict["attacklv75"] = int(value)
            elif index == 18 and newdict["slvmax"] >= 20:
                newdict["hplv150"] = int(value)
            elif index == 19 and newdict["slvmax"] >= 20:
                newdict["attacklv150"] = int(value)

        newdict["imageURL"] = "./imgs/" + key

        if name in translation:
            newdict["en"] = translation[name]
        else:
            print("missing translate", name)
            newdict["en"] = name

        json_data[name] = newdict
        # Wiki
        image_wiki_url_list.append("http://gbf-wiki.com/index.php?plugin=attach&refer=img&openfile=" + key + "\n")
        # Game - Might get you banned...
        image_game_url_list.append("http://gbf.game-a.mbga.jp/assets/img/sp/assets/weapon/b/" + key + "\n")
        image_wiki_url_list = list(OrderedDict.fromkeys(image_wiki_url_list))
        image_game_url_list = list(OrderedDict.fromkeys(image_game_url_list))

    return json_data, image_wiki_url_list, image_game_url_list


if __name__ == '__main__':
    json_data = OrderedDict()
    image_wiki_url_list = []
    image_game_url_list = []

    json_data, image_wiki_url_list, image_game_url_list = processCSVdata(
        os.path.join(path, "../txt_source/armData-ssr.txt"), json_data, image_wiki_url_list, image_game_url_list, True)
    json_data, image_wiki_url_list, image_game_url_list = processCSVdata(
        os.path.join(path, "../txt_source/armData-sr.txt"), json_data, image_wiki_url_list, image_game_url_list, False)

    f = open(os.path.join(path, "../armData.json"), "w", encoding="utf-8")
    json.dump(json_data, f, ensure_ascii=False, indent=4)
    f.close()

    f = open(os.path.join(path, "../txt_source/armImageWikiURLList.txt"), "w", encoding="utf-8")
    for x in image_wiki_url_list:
        f.write(x)
    f.close()
    f = open(os.path.join(path, "../txt_source/armImageGameURLList.txt"), "w", encoding="utf-8")
    for x in image_game_url_list:
        f.write(x)
    f.close()
