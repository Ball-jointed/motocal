import csv
import inspect
import json
import os
import re
from collections import OrderedDict

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

charatypelist = OrderedDict()
charatypelist[u"攻撃"] = "attack"
charatypelist[u"防御"] = "defense"
charatypelist[u"回復"] = "heal"
charatypelist[u"バランス"] = "balance"
charatypelist[u"特殊"] = "pecu"

racelist = OrderedDict()
racelist[u"ヒューマン/エルーン"] = "human/erune"
racelist[u"ヒューマン/ドラフ"] = "human/doraf"
racelist[u"ヒューマン"] = "human"
racelist[u"ドラフ"] = "doraf"
racelist[u"エルーン/ドラフ"] = "erune/doraf"
racelist[u"エルーン"] = "erune"
racelist[u"ハーヴィン/ヒューマン"] = "havin/human"
racelist[u"ハーヴィン"] = "havin"
racelist[u"星晶獣"] = "seisho"
racelist[u"不明"] = "unknown"
racelist[u"その他"] = "unknown"

sexlist = OrderedDict()
sexlist[u"男&br;女"] = "male/female"
sexlist[u"男"] = "male"
sexlist[u"女"] = "female"
sexlist[u"不明"] = "other"

############################################## Support Ability / サポートアビリティ##############################################

supportAbilist = OrderedDict()
supportAbilist["none"] = {
    u"剣聖を継ぐ者",  # NOTE: Avoid mis-matches with "剣聖"
}
# 味方全体のダブルアタック確率UP(10%)
supportAbilist["da_up_all_10"] = {
    u"双剣乱舞"
}
# 味方全体のトリプルアタック確率UP(3%)
supportAbilist["ta_up_all_3"] = {
    u"大いなる翼"
}
# 風属性キャラの連続攻撃確率UP(DA10%/TA5%)
supportAbilist["data_up_wind_10_5"] = {
    u"溢れる母性"
}
# 水属性キャラの連続攻撃確率UP(DA10%/TA5%)
supportAbilist["data_up_water_10_5"] = {
    u"舞い歌う夏の巫女"
}
# 得意武器「格闘」キャラのダブルアタック確率UP(10%)
supportAbilist["da_up_fist_10"] = {
    u"古今無双流"
}
supportAbilist["hp_down_own_15"] = {
    u"喪失する自我",
    u"アストラルチャージ"
}
supportAbilist["hp_up_own_10"] = {
    u"黒の鎧"
}
supportAbilist["hp_up_own_15"] = {
    u"やばいですね☆"
}
supportAbilist["hp_up_own_20"] = {
    u"本物のヒーロー"
}
supportAbilist["hp_up_own_30"] = {
    u"老當益壮"
}
supportAbilist["atk_up_own_5"] = {
    u"愛憎の衝動"
}
# 味方全体の攻撃UP(5%)
supportAbilist["atk_up_all_5"] = {
    u"クイーン・オブ・カジノ",
    u"ディペンデンス"
}
# 工事が必要
supportAbilist["atk_up_all_10"] = {
    u"羊神宮の主"
}
# 工事が必要
supportAbilist["atk_up_doraf"] = {
    u"質実剛健"
}
supportAbilist["atk_up_depends_races"] = {
    u"氷晶宮の特使"
}
supportAbilist["element_buff_boost_own_30"] = {
    u"王者の風格SR",
    #    u"覇者の風格"
}
supportAbilist["eternal_wisdom"] = {
    u"久遠の叡智"
}
supportAbilist["ougi_gage_up_own_10"] = {
    u"戦賢の書"
}
supportAbilist["ougi_gage_up_own_20"] = {
    u"剣聖",
    u"静かな威圧",
    u"片翼の悪魔",
    u"見た目は子供、頭脳は大人"
}
supportAbilist["ougi_gage_up_own_100"] = {
    u"刀神"
}
supportAbilist["ougi_gage_down_own_25"] = {
    u"砂神グラフォスの鉄槌",
    u"亥之一番"
}
supportAbilist["ougi_gage_down_own_35"] = {
    u"闘争求む重鎧"
}
supportAbilist["ougi_gage_down_own_35_ta_100"] = {
    u"ケンプファー",
    u"凶爪",
    u"バレンタインとか興味無いかな～",
    u"ワンダフルマジック",
}
supportAbilist["ougi_gage_up_djeeta_20"] = {
    u"クラリスちゃんの特製チョコ☆"
}
supportAbilist["ougi_damage_up_50_cap_10"] = {
    u"天星剣王2"
}
supportAbilist["ougi_damage_up_50"] = {
    u"天星剣王"
}
supportAbilist["ougi_damage_up_10"] = {
    u"音ノ木坂学院2年生"
}
supportAbilist["emnity_all_SL10"] = {
    u"太陽信仰",
    u"七回忌の砌",
    u"影歩む黒涙",
}
supportAbilist["emnity_own_SL20"] = {
    u"ダーク・ラピュセル",
    u"砂神グラフォスの慈愛",
}
supportAbilist["emnity_own_SL20_steps"] = {
    u"絶望の剣",
    u"ノートラーガ",
    u"無為の封縛",
}
supportAbilist["envoy_meditation"] = {
    u"調停の使徒"
}
supportAbilist["ideal_vassals"] = {
    u"理想の家臣"
}
supportAbilist["dance_of_nataraja"] = {
    u"破滅の舞踏"
}
supportAbilist["recklessness_incarnate"] = {
    u"猪突・上宝沁金ノ撃槍"
}
supportAbilist["knightmare_frame"] = {
    u"人型自在戦闘装甲騎",
    u"ナイトメアフレーム"
}
supportAbilist["sumizome_sakura"] = {
    u"墓前の墨染桜",
    u"浜辺の鋼鉄少女"
}
supportAbilist["arvess_pact"] = {
    u"アルベスの契約者"
}
supportAbilist["critical_up_own_10_30"] = {
    u"セルフィッシュ・ロイヤル",
    u"ラ・ピュセル30"
}
supportAbilist["critical_up_own_20_20"] = {
    u"ラ・ピュセル20"
}
supportAbilist["critical_up_own_40_50"] = {
    u"ぶっ殺すわよ！"
}
supportAbilist["critical_up_all_5_30"] = {
    u"調教してやる"
}
supportAbilist["mamoritai_kono_egao"] = {
    u"護りたい、この笑顔"
}
supportAbilist["mamorubeshi_sono_egao"] = {
    u"護るべし、その笑顔"
}
# The effect size of "真っ二つにしてやるんだっ！" has not been verified.
supportAbilist["damageUP_5"] = {
    u"真っ二つにしてやるんだっ！"
}
#supportAbilist["damageUP_10"] = {u""}
supportAbilist["damageUP_20"] = {
    u"炎帝の刃",
    u"冷たい女",
    u"アニマ・アエテルヌス",
    u"真龍の鉤爪",
    u"護国の双剣",
    u"アニマ・ドゥクトゥス",
}
supportAbilist["damageUP_OugiCapUP_20"] = {
    u"羅刹の豪槍",
    u"暴虎",
    u"死の舞踏",
    u"カンピオーネ",
    u"鬼神",
    u"惑乱の旋律",
    u"ピースメーカー",
}
supportAbilist["ougiCapUP_20"] = {
    u"孤高の狙撃手",
    u"天性の才能",
    u"反撃の狼煙",
}
supportAbilist["ougiCapUP_25"] = {
    u"生命のリンク",
    u"リレーション・コンバーター",
    u"ぎゃうー……",
}
supportAbilist["ougiCapUP_100"] = {
    u"神魔を恐れぬ王"
}
supportAbilist["wildcard"] = {
    u"ワイルドカード"
}
supportAbilist["hanged_man_reversed"] = {
    u"刑死者の逆位置"
}
# supportAbilist["fumetsu_no_mikiri"] = {
#     u"不滅の見切り"
# }
supportAbilist["aegisUP_30"] = {
    u"護国の双肩"
}
# supportAbilist["chikara_atsu_no_ha"] = {
#    u"力圧の刃"
# }
supportAbilist["more_than_mere_speed"] = {
    u"ビヨンド・ザ・スピード"
}
supportAbilist["no_multi_attack"] = {
    u"ナイトロ・リミッター"
}
supportAbilist["element_buff_boost_fire_30"] = {
    u"崇拝の尊神"
}
supportAbilist["element_buff_boost_water_30"] = {
    u"神虜の麗姫"
}
supportAbilist["element_buff_boost_earth_30"] = {
    u"神域の守護者"
}
supportAbilist["element_buff_boost_wind_30"] = {
    u"踊り狂う暴風"
}
supportAbilist["element_buff_boost_light_30"] = {
    u"聖布の乙女"
}
# supportAbilist["element_buff_boost_dark_30"] = {
#     u""
# }
# supportAbilist["element_buff_boost_all_30"] = {
#     u""
# }
supportAbilist["element_buff_boost_wind_15"] = {
    u"精霊の啓示"
}
supportAbilist["critical_cap_up_water_3"] = {
    u"正射必中"
}
supportAbilist["critical_cap_up_light_3"] = {
    u"スポッター"
}
supportAbilist["critical_cap_up_earth_3"] = {
    u"遥かな夜空に思いを馳せて"
}
supportAbilist["crazy_auguste"] = {
    u"頭アウギュステ"
}
supportAbilist["lillie_liebe"] = {
    u"リーリエ・リーベ"
}
supportAbilist["sandy_sniper"] = {
    u"砂浜のスナイパー"
}
supportAbilist["unwavering_conviction"] = {
    u"揺るぎない信念"
}
supportAbilist["shinryu_to_no_kizuna"] = {
    u"真龍との絆"
}
supportAbilist["revion_kishi_sanshimai"] = {
    u"レヴィオン騎士三姉妹"
}
supportAbilist["element_buff_boost_damageUP_own_10"] = {
    #    u"堕天司"
}
supportAbilist["element_buff_boost_damageUP_normal_own_30"] = {
    u"堕天司"
}
# supportAbilist["no_normal_attack"] = {
#     u"優しい心",
#     u"カードキャプター"
# }
# supportAbilist["tousou_no_chishio"] = {
#     u"闘争の血潮"
# }
supportAbilist["kenkyaku_no_koou"] = {
    u"剣脚の呼応"
}
supportAbilist["kenkyaku_no_koou"] = {
    u"剣脚の呼応"
}
supportAbilist["debuff_resistance_up_own_15"] = {
    u"ユニバーサルスター",
    u"魔生花の楔"
}
supportAbilist["debuff_resistance_up_own_80"] = {
    u"魔道の申し子"
}
supportAbilist["stamina_all_L"] = {
    u"夏祭りの思い出",
    u"不退転の戦旗",
    u"絶対だいじょうぶだよ",
    u"マップタツパワー"
}
supportAbilist["stamina_all_M"] = {
    u"黒の騎士団 総司令"
}
supportAbilist["stamina_all_L_hp_down_own_15"] = {
    u"真夏の夜の夢"
}
supportAbilist["supplemental_third_hit_50k"] = {
    u"みんなのあんぜんあんしん",
    u'炎天の雷迅卿'
}
supportAbilist["benedikutosu_soure"] = {
    u"太陽の逆位置"  # placeholder for ougi effect not the support ability effect
}
supportAbilist["otherbuff_own_30"] = {
    u"アインザーム"
}
supportAbilist["party_all_night"] = {
    u"朝までハッピィ～！"
}
# 光属性キャラがトリプルアタック時に風属性追撃効果(10%)
supportAbilist["additional_damage_on_ta_light_10"] = {
    u"ドレス・ラ・ピュセル"
}
# 風属性キャラがトリプルアタック時に風属性追撃効果(10%)
supportAbilist["additional_damage_on_ta_wind_10"] = {
    u"真夏の我は一味違うぞ？"
}
supportAbilist["ougi_gage_down_own_50_damageUP_25"] = {
    u"征道の書"
}
supportAbilist["da_up_ta_up_damageUPOnlyNormal_fist_10_5_3"] = {
    u"己の意志"
}
supportAbilist["element_buff_boost_other_own_30"] = {
    u"真龍の友愛"
}

############################## Double Attack and Triple Attack Rate / ダブルアタック、トリプルアタック確率 ###############################

patching = OrderedDict()

# Consecutive atk rate from すんどめ侍さん
# Default: DA7%,TA3%

# Eternals
patching["[超越]ソーン"] = {"DA": 4.0, "TA": 1.0}
patching["[超越]サラーサ"] = {"DA": 5.0, "TA": 2.0}
patching["[超越]カトル"] = {"DA": 10.0, "TA": 5.0}
patching["[超越]フュンフ"] = {"DA": 4.0, "TA": 1.0}
patching["[超越]シス"] = {"DA": 1000.0, "TA": 0.0}
patching["[超越]シエテ"] = {"DA": 10.0, "TA": 5.0}
patching["[超越]オクトー"] = {"DA": 25.0, "TA": 2.0}  # Support skill DA20%
patching["[超越]ニオ"] = {"DA": 4.0, "TA": 1.0}
patching["[超越]エッセル"] = {"DA": 10.0, "TA": 5.0}
patching["[超越]ソーン"] = {"DA": 4.0, "TA": 1.0}
patching["[最終]サラーサ"] = {"DA": 5.0, "TA": 2.0}
patching["[最終]カトル"] = {"DA": 10.0, "TA": 5.0}
patching["[最終]フュンフ"] = {"DA": 4.0, "TA": 1.0}
patching["[最終]シス"] = {"DA": 1000.0, "TA": 0.0}
patching["[最終]シエテ"] = {"DA": 10.0, "TA": 5.0}
patching["[最終]オクトー"] = {"DA": 25.0, "TA": 2.0}  # Support skill DA20%
patching["[最終]ニオ"] = {"DA": 4.0, "TA": 1.0}
patching["[最終]エッセル"] = {"DA": 10.0, "TA": 5.0}
patching["ソーン"] = {"DA": 4.0, "TA": 1.0}
patching["サラーサ"] = {"DA": 5.0, "TA": 2.0}
patching["カトル"] = {"DA": 10.0, "TA": 5.0}
patching["フュンフ"] = {"DA": 4.0, "TA": 1.0}
patching["シス"] = {"DA": 1000.0, "TA": 0.0}
patching["シエテ"] = {"DA": 10.0, "TA": 5.0}
patching["オクトー"] = {"DA": 5.0, "TA": 2.0}
patching["ニオ"] = {"DA": 4.0, "TA": 1.0}
patching["エッセル"] = {"DA": 10.0, "TA": 5.0}

## 火 - Fire
patching["ゼタ"] = {"DA": 10.0, "TA": 5.0}
patching["ラカム(リミテッドver)"] = {"DA": 10.0, "TA": 5.0}
patching["テレーズ(SSR)"] = {"DA": 10.0, "TA": 5.0}
patching["メーテラ(火属性ver)"] = {"DA": 10.0, "TA": 5.0}
patching["ヘルエス"] = {"DA": 10.0, "TA": 5.0}
patching["ガンダゴウザ"] = {"DA": 10.0, "TA": 5.0}
patching["アリーザ(SSR)"] = {"DA": 10.0, "TA": 5.0}
patching["グレア"] = {"DA": 10.0, "TA": 5.0}
patching["スツルム"] = {"DA": 10.0, "TA": 5.0}
patching["アラナン"] = {"DA": 10.0, "TA": 5.0}
patching["パーシヴァル"] = {"DA": 10.0, "TA": 5.0}
patching["ニーナ・ドランゴ"] = {"DA": 10.0, "TA": 5.0}
patching["紅月カレン"] = {"DA": 10.0, "TA": 5.0}
patching["フラウ"] = {"DA": 10.0, "TA": 5.0}
patching["ユエル"] = {"DA": 12.0, "TA": 3.0}  # Support skill DA5%
patching["アオイドス"] = {"DA": 4.0, "TA": 1.0}
patching["アニラ"] = {"DA": 4.0, "TA": 1.0}
patching["アギエルバ"] = {"DA": 4.0, "TA": 1.0}
patching["ザルハメリナ"] = {"DA": 4.0, "TA": 1.0}
patching["イオ(水着ver)"] = {"DA": 4.0, "TA": 1.0}
patching["白竜の双騎士 ランスロット＆ヴェイン"] = {"DA": 1000.0, "TA": 3.0}

# SR
patching["ジェミニ・サンライズ"] = {"DA": 10.0, "TA": 5.0}
patching["テレーズ(バニーver)"] = {"DA": 10.0, "TA": 5.0}
patching["天道輝"] = {"DA": 10.0, "TA": 5.0}
patching["神月かりん"] = {"DA": 10.0, "TA": 5.0}

## 水 - Water
patching["イングヴェイ"] = {"DA": 10.0, "TA": 5.0}
patching["シルヴァ"] = {"DA": 10.0, "TA": 5.0}
patching["ランスロット(SSR)"] = {"DA": 10.0, "TA": 5.0}
patching["桜内梨子＆高海千歌＆渡辺 曜"] = {"DA": 10.0, "TA": 5.0}
patching["ヴァジラ"] = {"DA": 10.0, "TA": 5.0}
patching["ユエル(水属性ver)"] = {"DA": 10.0, "TA": 5.0}
patching["ソシエ"] = {"DA": 20.0, "TA": 5.0}  # Support skill DA10%
patching["イシュミール"] = {"DA": 10.0, "TA": 5.0}
patching["グレア(水着ver)"] = {"DA": 10.0, "TA": 5.0}
patching["リリィ"] = {"DA": 4.0, "TA": 1.0}
patching["エウロペ"] = {"DA": 4.0, "TA": 1.0}
patching["ダヌア(ハロウィンver)"] = {"DA": 4.0, "TA": 1.0}

# SR
patching["アンジェ"] = {"DA": 12.0, "TA": 3.0}  # Support skill DA5%
patching["テレーズ"] = {"DA": 10.0, "TA": 5.0}
patching["春麗"] = {"DA": 10.0, "TA": 5.0}
patching["オーウェン"] = {"DA": 1000.0, "TA": 3.0}

## 土 - Earth
patching["アレーティア"] = {"DA": 10.0, "TA": 5.0}
patching["ヴィーラ(水着ver)"] = {"DA": 10.0, "TA": 5.0}
patching["キャサリン"] = {"DA": 10.0, "TA": 5.0}
patching["ネモネ"] = {"DA": 10.0, "TA": 5.0}
patching["ユーステス(ハロウィンver)"] = {"DA": 10.0, "TA": 5.0}
patching["ダーント＆フライハイト"] = {"DA": 10.0, "TA": 5.0}
patching["カリオストロ"] = {"DA": 4.0, "TA": 1.0}
patching["サラ"] = {"DA": 4.0, "TA": 1.0}
patching["レ・フィーエ(土属性ver)"] = {"DA": 4.0, "TA": 1.0}
patching["津島善子＆国木田花丸＆黒澤ルビィ"] = {"DA": 4.0, "TA": 1.0}
patching["真紅と冥闇 ゼタ＆バザラガ(ハロウィンver)"] = {"DA": 1000.0, "TA": 3.0}
patching["メルゥ"] = {"DA": 12.0, "TA": 3.0}

# SR
patching["カルメリーナ(SR)"] = {"DA": 4.0, "TA": 1.0}
patching["白竜の双騎士 ランスロット＆ヴェイン(SR)(水着ver)"] = {"DA": 1000.0, "TA": 3.0}

## 風 - Wind
patching["ユエル(水着ver)"] = {"DA": 12.0, "TA": 3.0}
patching["コッコロ"] = {"DA": 12.0, "TA": 3.0}
patching["ヘルエス(風属性ver)"] = {"DA": 10.0, "TA": 5.0}
patching["メリッサベル"] = {"DA": 10.0, "TA": 5.0}
patching["スカーサハ"] = {"DA": 10.0, "TA": 5.0}
patching["ジャンヌダルク(水着ver)"] = {"DA": 10.0, "TA": 5.0}
patching["ジークフリート(浴衣ver)"] = {"DA": 10.0, "TA": 5.0}
patching["コルワ"] = {"DA": 4.0, "TA": 1.0}
patching["コルワ(水着ver)"] = {"DA": 4.0, "TA": 1.0}
patching["フィーナ(SSR)"] = {"DA": 4.0, "TA": 1.0}
patching["カルメリーナ"] = {"DA": 4.0, "TA": 1.0}
patching["リヴァイ"] = {"DA": 0.0, "TA": 100.0}
patching["勇者と姫君 スタン＆アリーザ"] = {"DA": 1000.0, "TA": 3.0}
patching["ミュオン(クリスマスver)"] = {"DA": 0, "TA": 1000.0}
patching["グリームニル(バレンタインver)"] = {"DA": 1000.0, "TA": 1000.0}

# SR
patching["リュウ"] = {"DA": 10.0, "TA": 5.0}
patching["フィーナ"] = {"DA": 4.0, "TA": 1.0}

## 光 - Light
patching["アーミラ(SSR)"] = {"DA": 10.0, "TA": 5.0}
patching["ゼタ(水着ver)"] = {"DA": 10.0, "TA": 5.0}
patching["ヘルエス(水着ver)"] = {"DA": 10.0, "TA": 5.0}
patching["ジャンヌダルク"] = {"DA": 10.0, "TA": 5.0}
patching["セルエル"] = {"DA": 10.0, "TA": 5.0}
patching["ロザミア(SSR)"] = {"DA": 10.0, "TA": 5.0}
patching["メリッサベル(バレンタインver)"] = {"DA": 10.0, "TA": 5.0}
patching["メーテラ(クリスマスver)"] = {"DA": 10.0, "TA": 5.0}
patching["シルヴァ(光属性ver)"] = {"DA": 10.0, "TA": 5.0}
patching["ルシオ(リミテッドver)"] = {"DA": 10.0, "TA": 5.0}
patching["ガイゼンボーガ"] = {"DA": 10.0, "TA": 5.0}
patching["バウタオーダ(SSR)"] = {"DA": 4.0, "TA": 1.0}
patching["イオ(リミテッドver)"] = {"DA": 4.0, "TA": 1.0}
patching["ソフィア"] = {"DA": 4.0, "TA": 1.0}
patching["レ・フィーエ(水着ver)"] = {"DA": 4.0, "TA": 1.0}
patching["シャルロッテ(ハロウィンver)"] = {"DA": 4.0, "TA": 1.0}
patching["アルベール"] = {"DA": 1000.0, "TA": 3.0}
patching["プリキュア"] = {"DA": 1000.0, "TA": 3.0}
patching["レヴィオン姉妹 マイム＆ミイム＆メイム"] = {"DA": 1000.0, "TA": 3.0}
patching["ハールート・マールート(水着ver)"] = {"DA": 1000.0, "TA": 3.0}
patching["ハレゼナ(ハロウィンver)"] = {"DA": 1000.0, "TA": 1000.0}
patching["渋谷凛＆島村卯月＆本田未央"] = {"DA": 1000.0, "TA": 1000.0}

# SR
patching["ゼタ(SR)"] = {"DA": 10.0, "TA": 5.0}
patching["フェリ(ハロウィンver)"] = {"DA": 10.0, "TA": 5.0}
patching["アンジェ(ハロウィンver)"] = {"DA": 12.0, "TA": 3.0}  # Support skill DA5%
patching["フィーナ(クリスマスver)"] = {"DA": 4.0, "TA": 1.0}
patching["アルベール(SR)"] = {"DA": 1000.0, "TA": 3.0}

## 闇 - Dark
patching["フォルテ"] = {"DA": 10.0, "TA": 5.0}
patching["ゼタ(闇属性ver)"] = {"DA": 10.0, "TA": 5.0}
patching["ヴィーラ(SSR)"] = {"DA": 10.0, "TA": 5.0}
patching["黒騎士(リミテッドver)"] = {"DA": 10.0, "TA": 5.0}
patching["レディ・グレイ"] = {"DA": 10.0, "TA": 5.0}
patching["ジャンヌダルク(闇)"] = {"DA": 10.0, "TA": 5.0}
patching["アザゼル"] = {"DA": 10.0, "TA": 5.0}
patching["バザラガ"] = {"DA": 4.0, "TA": 1.0}
patching["ダヌア(水着ver)"] = {"DA": 4.0, "TA": 1.0}
patching["カリオストロ(闇属性ver)"] = {"DA": 4.0, "TA": 1.0}
patching["ベアトリクス"] = {"DA": 4.0, "TA": 1.0}
patching["ウーフとレニー"] = {"DA": 1000.0, "TA": 1000.0}
patching["ケルベロス"] = {"DA": 0.0, "TA": 55.0}
patching["ユーステス(闇属性ver)"] = {"DA": 13.0, "TA": 5.5}
patching["プレデター(SSR)"] = {"DA": 1000.0, "TA": 1000.0}

# SR
patching["プレデター"] = {"DA": 1000.0, "TA": 1000.0}


################################################### Charge Attack ratio / 奥義倍率 #########################################
# Verification list: https://docs.google.com/spreadsheets/d/1kea2IL6wLNbw4RNUcrrxMTpoIdlXU13pYOzBXjgoBbs/edit#gid=199555968

patchingOugiRatio = OrderedDict()

defaultOugiRatio = {"SSR": 4.5, "SR": 3.5, "R": 3.5,}

# 5★ SSR Characters / 最終上限解放SSRキャラ (奥義倍率5.0倍)
patchingOugiRatio["[最終]レディ・グレイ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]バザラガ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ナルメア"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ヴィーラ(SSR)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ジャンヌダルク"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]セルエル"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]サルナーン"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]アーミラ(SSR)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]レナ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ネツァワルピリ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ガウェイン"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ハレゼナ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ジークフリート"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]カリオストロ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]アルルメイヤ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ランスロット(SSR)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]シルヴァ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]シャルロッテ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]イングヴェイ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]アルタイル"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ユエル"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]マギサ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]パーシヴァル"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]スカーサハ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ガンダゴウザ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]メーテラ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]アルベール"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]桜内梨子＆高海千歌＆渡辺 曜"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]サンダルフォン"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ヴァンピィ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]リリィ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]アイル"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]カタリナ(リミテッドver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ラカム(リミテッドver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]黒騎士(リミテッドver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ゼタ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ティアマト"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ヴェイン(SSR)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]イオ(リミテッドver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]アオイドス"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]クリスティーナ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ソリッズ(SSR)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ロミオ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]絢瀬絵里＆矢澤にこ＆東條 希"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]イシュミール"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]オーキス(リミテッドver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]メルゥ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ユーステス(闇属性ver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ソシエ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ユリウス"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]オイゲン(リミテッドver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]アテナ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ユグドラシル"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ヘルエス"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ケルベロス"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ルナール"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ロゼッタ(リミテッドver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ゾーイ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ヴィーラ(リミテッドver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ユイシス"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]アレーティア"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ガウェイン(光属性ver)"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]アン"] = {"ougiRatio": 5.0}

# SSR Guardian Deity / 十二神将 (奥義倍率5.0倍)
patchingOugiRatio["アニラ"] = {"ougiRatio": 5.0}
patchingOugiRatio["アンチラ"] = {"ougiRatio": 5.0}
patchingOugiRatio["マキラ"] = {"ougiRatio": 5.0}
patchingOugiRatio["ヴァジラ"] = {"ougiRatio": 5.0}
patchingOugiRatio["クビラ"] = {"ougiRatio": 5.0}
patchingOugiRatio["ビカラ"] = {"ougiRatio": 5.0}
patchingOugiRatio["シャトラ"] = {"ougiRatio": 5.0}
patchingOugiRatio["シンダラ"] = {"ougiRatio": 5.0}

# 5★ SSR Guardian Deity / 最終上限解放十二神将 (奥義倍率5.5倍)
patchingOugiRatio["[最終]アニラ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[最終]アンチラ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[最終]マキラ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[最終]ヴァジラ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[最終]クビラ"] = {"ougiRatio": 5.5}

# 5★ The Eternals / 最終上限解放十天衆 (奥義倍率5.0倍)
patchingOugiRatio["[最終]ウーノ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ソーン"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]サラーサ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]カトル"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]フュンフ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]シス"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]シエテ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]オクトー"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]ニオ"] = {"ougiRatio": 5.0}
patchingOugiRatio["[最終]エッセル"] = {"ougiRatio": 5.0}

# 6★ The Eternals / 限界超越十天衆 (奥義倍率5.5倍)
patchingOugiRatio["[超越]ウーノ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[超越]ソーン"] = {"ougiRatio": 5.5}
patchingOugiRatio["[超越]サラーサ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[超越]カトル"] = {"ougiRatio": 5.5}
patchingOugiRatio["[超越]フュンフ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[超越]シス"] = {"ougiRatio": 5.5}
patchingOugiRatio["[超越]シエテ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[超越]オクトー"] = {"ougiRatio": 5.5}
patchingOugiRatio["[超越]ニオ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[超越]エッセル"] = {"ougiRatio": 5.5}

# Other SSR Characters / その他、特殊な奥義倍率を持つSSRキャラ
patchingOugiRatio["アギエルバ"] = {"ougiRatio": 4.7}
patchingOugiRatio["イオ(水着ver)"] = {"ougiRatio": 4.7}
patchingOugiRatio["レ・フィーエ(水着ver)"] = {"ougiRatio": 4.7}
patchingOugiRatio["シャルロッテ(ハロウィンver)"] = {"ougiRatio": 4.7}
patchingOugiRatio["ロゼッタ(クリスマスver)"] = {"ougiRatio": 4.7}
patchingOugiRatio["サラ"] = {"ougiRatio": 5.0}
patchingOugiRatio["レ・フィーエ"] = {"ougiRatio": 5.5}
patchingOugiRatio["[最終]レ・フィーエ"] = {"ougiRatio": 6.0}
patchingOugiRatio["ミュオン(クリスマスver)"] = {"ougiRatio": 10.5}

# Unworldly Charge Attack SSR Charactters / (極大)持ちSSRキャラ (奥義倍率10.0 - 12.5倍)
patchingOugiRatio["シャリオス17世"] = {"ougiRatio": 12.5}
patchingOugiRatio["ロボミ(SSR)"] = {"ougiRatio": 12.5}
patchingOugiRatio["コロッサス"] = {"ougiRatio": 12.5}
patchingOugiRatio["飛竜と吸血姫 ヴァンピィ＆ベス"] = {"ougiRatio": 12.5}
patchingOugiRatio["シュラ"] = {"ougiRatio": 12.5}
patchingOugiRatio["アーミラ(水着ver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["ミムルメモル(水着ver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["煉獄杏寿郎"] = {"ougiRatio": 12.5}
patchingOugiRatio["ネクタル"] = {"ougiRatio": 10.0}
patchingOugiRatio["ゼタ(水属性ver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["バザラガ(火属性ver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["ベアトリクス(土属性ver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["ナルメア(リミテッドver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["イシュミール(水着ver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["シヴァ(水着ver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["ウィルナス(リミテッドver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["シルヴァ(浴衣ver)"] = {"ougiRatio": 12.5}
patchingOugiRatio["ワムデュス(リミテッドver)"] = {"ougiRatio": 12.5}

# No DMG Charge Attack SSR Charactters / ダメージ無し奥義持ちSSRキャラ (奥義倍率0.0倍)
patchingOugiRatio["ソフィア"] = {"ougiRatio": 0.0}
patchingOugiRatio["コルワ"] = {"ougiRatio": 0.0}
patchingOugiRatio["コルワ(水着ver)"] = {"ougiRatio": 0.0}
patchingOugiRatio["コッコロ"] = {"ougiRatio": 0.0}
patchingOugiRatio["ディアンサ(水着ver)"] = {"ougiRatio": 0.0}
patchingOugiRatio["木之本桜"] = {"ougiRatio": 0.0}
patchingOugiRatio["グリームニル(バレンタインver)"] = {"ougiRatio": 0.0}
patchingOugiRatio["レイ(リミテッドver)"] = {"ougiRatio": 0.0}
patchingOugiRatio["ディアンサ(SSR)"] = {"ougiRatio": 0.0}
patchingOugiRatio["ネハン(リミテッドver)"] = {"ougiRatio": 0.0}
patchingOugiRatio["ソフィア(水属性ver)"] = {"ougiRatio": 0.0}
patchingOugiRatio["ビカラ(水着ver)"] = {"ougiRatio": 0.0}
patchingOugiRatio["ティコ(水着ver)"] = {"ougiRatio": 0.0}

# 5★ SR Characters / 最終上限解放SRキャラ (奥義倍率4.0倍)
patchingOugiRatio["[最終]ヘルナル"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]カタリナ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]イオ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]オイゲン"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ラカム"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ガイーヌ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]アンジェ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ウラムヌラン"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ダヌア"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]スーテラ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ソリッズ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]セレフィラ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ルシウス"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ティナ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ノア"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]島村卯月"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]渋谷凛"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]城ヶ崎美嘉"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]本田未央"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]リタ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]エジェリー"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]アーミラ(SR)"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]双葉杏"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]フェザー"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]城ヶ崎莉嘉"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ウィル"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ノイシュ(火属性ver)"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]シャオ"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ミュオン"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ウェルダー(イベントver)"] = {"ougiRatio": 4.0}
patchingOugiRatio["[最終]ミリン"] = {"ougiRatio": 4.0}

# Other SR Characters / その他、特殊な奥義倍率を持つSRキャラ
patchingOugiRatio["[最終]アレク"] = {"ougiRatio": 4.2}
patchingOugiRatio["カタリナ(水着ver)"] = {"ougiRatio": 3.7}
patchingOugiRatio["ヘルナル(水着ver)"] = {"ougiRatio": 3.7}
patchingOugiRatio["アンジェ(ハロウィンver)"] = {"ougiRatio": 3.7}
patchingOugiRatio["ルリア"] = {"ougiRatio": 6.0}
patchingOugiRatio["[最終]ルリア"] = {"ougiRatio": 7.0}
patchingOugiRatio["チーム・ローアイン"] = {"ougiRatio": 10.0}

# No DMG Charge Attack SR Charactters / ダメージ無し奥義持ちSRキャラ (奥義倍率0.0倍)
patchingOugiRatio["ヤイア"] = {"ougiRatio": 0.0}
patchingOugiRatio["[最終]ヤイア"] = {"ougiRatio": 0.0}
patchingOugiRatio["ローアイン(SR)"] = {"ougiRatio": 0.0}
patchingOugiRatio["[最終]ローアイン(SR)"] = {"ougiRatio": 0.0}
patchingOugiRatio["エリカ・フォンティーヌ"] = {"ougiRatio": 0.0}
patchingOugiRatio["ディアンサ"] = {"ougiRatio": 0.0}
patchingOugiRatio["ルドミリア"] = {"ougiRatio": 0.0}
patchingOugiRatio["一ノ瀬志希"] = {"ougiRatio": 0.0}
patchingOugiRatio["クロエ(水着ver)"] = {"ougiRatio": 0.0}
patchingOugiRatio["ソフィア(SR)"] = {"ougiRatio": 0.0}
patchingOugiRatio["カルメリーナ(SR)"] = {"ougiRatio": 0.0}
patchingOugiRatio["リルル(水着ver)"] = {"ougiRatio": 0.0}

# Other R Characters / その他、特殊な奥義倍率を持つRキャラ
patchingOugiRatio["猫"] = {"ougiRatio": 2.0}

# No DMG Charge Attack R Charactters / ダメージ無し奥義持ちRキャラ (奥義倍率0.0倍)
patchingOugiRatio["クロエ"] = {"ougiRatio": 0.0}
patchingOugiRatio["ドロッセル"] = {"ougiRatio": 0.0}

########################################################################################################################
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

# json translation
translation = json.load(open(os.path.join(
    path, "../txt_source/chara-translation.json"), "r", encoding="utf-8"))


def arm_replace(armtype):
    for armtypename, inner_armtype in armtypelist.items():
        if re.match(armtypename, armtype):
            return inner_armtype
    print("favorite_arm_error")
    return "error"


def type_replace(charatype):
    for charatypename, inner_charatype in charatypelist.items():
        if re.match(charatypename, charatype):
            return inner_charatype
    print("charatype_error")
    return "error"


def race_replace(racetype):
    for racetypename, inner_racetype in racelist.items():
        if re.match(racetypename, racetype):
            return inner_racetype
    print("racetype_error")
    return "error"


def sex_replace(sextype):
    for sextypename, inner_sextype in sexlist.items():
        if re.match(sextypename, sextype):
            return inner_sextype
    print("sextype_error")
    return "error"


def support_replace(support_str):
    support_pattern = re.compile("\[\[([\W\w]+?)>")

    m = support_pattern.search(support_str)
    if m:
        support = m.group(1)
        for support_typename, support_name in supportAbilist.items():
            for name in support_name:
                if re.match(name, support):
                    return support_typename
    return "none"


def get_value(value_str):
    value_pattern = re.compile("(\d+)")
    matched = value_pattern.search(value_str)

    if matched:
        return matched.group(1)
    else:
        print("input: " + value_str)
        print("matched: error")
        return "error"


def processCSVdata(csv_file_name, json_data, image_wiki_url_list, image_game_url_list):
    key_pattern = re.compile("(\w+\.jpg)")
    br_pattern = re.compile("(\w+)(?:;|\/)(\w+)")
    support_pattern2 = re.compile("([\W\w]+)&br;([\W\w]+)")
    support_pattern3 = re.compile("([\W\w]+)&br;([\W\w]+)&br;([\W\w]+)")
    name_pattern = re.compile("\[\[([\W\w]+?) \((S?S?R)\)")

    mycsv = csv.reader(
        open(csv_file_name, 'r', encoding="utf-8"), delimiter="|")
    for row in mycsv:
        newdict = OrderedDict()

        if len(row) <= 1:
            continue
        else:
            m = key_pattern.search(row[1])
            if m:
                key = m.group(1)

            m = name_pattern.search(row[2])
            if m:
                name = m.group(1)
                rare = m.group(2)    # <- "SSR", "SR", "R"
            else:
                print("error")
                name = "error"

            newdict["name"] = name
            newdict["ja"] = name

            # element
            if row[3].find("火") >= 0:
                newdict["element"] = "fire"
            elif row[3].find("水") >= 0:
                newdict["element"] = "water"
            elif row[3].find("土") >= 0:
                newdict["element"] = "earth"
            elif row[3].find("風") >= 0:
                newdict["element"] = "wind"
            elif row[3].find("光") >= 0:
                newdict["element"] = "light"
            else:
                newdict["element"] = "dark"

            # type
            newdict["type"] = type_replace(row[4])
            newdict["race"] = race_replace(row[5])
            newdict["sex"] = sex_replace(row[6])

            m = br_pattern.search(row[7])
            if m:
                newdict["fav1"] = arm_replace(m.group(1))
                newdict["fav2"] = arm_replace(m.group(2))
            else:
                newdict["fav1"] = arm_replace(row[7])
                newdict["fav2"] = "none"

            m3 = support_pattern3.search(row[10])
            m2 = support_pattern2.search(row[10])
            if m3:
                newdict["support"] = support_replace(m3.group(1))
                newdict["support2"] = support_replace(m3.group(2))
                newdict["support3"] = support_replace(m3.group(3))
            elif m2:
                newdict["support"] = support_replace(m2.group(1))
                newdict["support2"] = support_replace(m2.group(2))
                newdict["support3"] = "none"
            else:
                newdict["support"] = support_replace(row[10])
                newdict["support2"] = "none"
                newdict["support3"] = "none"

            newdict["minhp"] = get_value(row[11])
            newdict["hp"] = get_value(row[13])

            newdict["minattack"] = get_value(row[12])
            newdict["attack"] = get_value(row[14])

            if newdict["name"] in patching:
                newdict["baseDA"] = patching[newdict["name"]]["DA"]
                newdict["baseTA"] = patching[newdict["name"]]["TA"]
            else:
                newdict["baseDA"] = 7.0
                newdict["baseTA"] = 3.0

            if newdict["name"] in patchingOugiRatio:
                newdict["ougiRatio"] = patchingOugiRatio[newdict["name"]]["ougiRatio"]
            else:
                newdict["ougiRatio"] = defaultOugiRatio[rare]

            newdict["imageURL"] = "./charaimgs/" + key

            if name in translation:
                newdict["en"] = translation[name]
            else:
                print(name)
                newdict["en"] = name

            json_data[name] = newdict
            # Wiki
            image_wiki_url_list.append(
                "http://gbf-wiki.com/index.php?plugin=attach&refer=img&openfile=" + key + "\n")
            # Game - Might get you banned...
            image_game_url_list.append(
                "http://gbf.game-a.mbga.jp/assets/img/sp/assets/npc/b/" + key + "\n")
            image_wiki_url_list = list(
                OrderedDict.fromkeys(image_wiki_url_list))
            image_game_url_list = list(
                OrderedDict.fromkeys(image_game_url_list))

    return json_data, image_wiki_url_list, image_game_url_list


if __name__ == '__main__':
    json_data = OrderedDict()
    image_wiki_url_list = []
    image_game_url_list = []

    json_data, image_wiki_url_list, image_game_url_list = processCSVdata(
        os.path.join(path, "../txt_source/charaData.txt"), json_data, image_wiki_url_list, image_game_url_list)

    f = open(os.path.join(path, "../charaData.json"), "w", encoding="utf-8")
    json.dump(json_data, f, ensure_ascii=False, indent=4)
    f.close()

    f = open(os.path.join(
        path, "../txt_source/charaImageWikiURLList.txt"), "w", encoding="utf-8")
    for x in image_wiki_url_list:
        # TODO: create chain of url replacements for every wrong jp wiki url on update
        r = x
        r = re.sub('3040183000_03.png', '3040183000_03_full.png', r)
        r = re.sub('3040153000_03.png', '3040153000_03_full.png', r)
        r = re.sub('3040152000_03.png', '3040152000_03_full.png', r)
        r = re.sub('3040122000_03.png', '3040122000_03_full.png', r)
        r = re.sub('3040107000_03.png', '3040107000_03_full.png', r)
        r = re.sub('3040082000_03.png', '3040082000_03_full.png', r)
        r = re.sub('3040076000_03.png', '3040076000_03_full.png', r)
        r = re.sub('3040071000_03.png', '3040071000_03_full.png', r)
        r = re.sub('3040065000_03.png', '3040065000_03_full.png', r)
        r = re.sub('3040063000_03.png', '3040063000_03_full.png', r)
        r = re.sub('3040059000_03.png', '3040059000_03_full.png', r)
        r = re.sub('3040057000_03.png', '3040057000_03_full.png', r)
        r = re.sub('3040054000_03.png', '3040054000_03_full.png', r)
        r = re.sub('3040052000_03.png', '3040052000_03_full.png', r)
        r = re.sub('3040049000_03.png', '3040049000_03_full.png', r)
        r = re.sub('3040045000_03.png', '3040045000_03_full.png', r)
        r = re.sub('3040029000_03.png', '3040029000_03_full.png', r)
        r = re.sub('3040028000_03.png', '3040028000_03_full.png', r)
        r = re.sub('3040021000_03.png', '3040021000_03_full.png', r)
        r = re.sub('3040019000_03.png', '3040019000_03_full.png', r)
        r = re.sub('3040018000_03.png', '3040018000_03_full.png', r)
        r = re.sub('3040012000_03.png', '3040012000_03_full.png', r)
        r = re.sub('3040008000_03.png', '3040008000_03_full.png', r)
        r = re.sub('3040007000_03.png', '3040007000_03_full.png', r)
        r = re.sub('3040004000_03.png', '3040004000_03full.png', r)
        r = re.sub('3040001000_03.png', '3040001000_03_full.png', r)
        r = re.sub('3030005000_03.png', '3030005000_03_full.png', r)
        r = re.sub('3030007000_03.png', '3030007000_03_full.png', r)
        r = re.sub('3030008000_03.png', '3030008000_03_full.png', r)
        r = re.sub('3030051000_03.png', '3030051000_03_full.png', r)
        r = re.sub('3030054000_03.png', '3030054000_03_full.png', r)
        r = re.sub('3030061000_03.png', '3030061000_03_full.png', r)
        r = re.sub('3030065000_03.png', '3030065000_03_full.png', r)
        r = re.sub('3030071000_03.png', '3030071000_03_full.png', r)
        r = re.sub('3030088000_03.png', '3030088000_03_full.png', r)
        r = re.sub('3030092000_03.png', '3030092000_03_full.png', r)
        r = re.sub('3030111000_03.png', '3030111000_03_full.png', r)
        r = re.sub('3030124000_03.png', '3030124000_03_full.png', r)
        r = re.sub('3030172000_03.png', '3030172000_03_full.png', r)
        r = re.sub('3030197000_03.png', '3030197000_03_full.png', r)
        r = re.sub('3030224000_03.png', '3030224000_03_full.png', r)
        r = re.sub('3040170000_03.png', '3040170000_03_full.png', r)
        r = re.sub('3040098000_03.png', '3040098000_03_full.png', r)
        f.write(r)
    f.close()

    f = open(os.path.join(
        path, "../txt_source/charaImageGameURLList.txt"), "w", encoding="utf-8")
    for x in image_game_url_list:
        f.write(x)
    f.close()
