import random
import re

emoji_span_str = '<span class="emoji emoji([\w]*)"></span>'
emoji_pattern = re.compile(emoji_span_str)


def gen_random_emotion():
    while True:
        try:
            qq_or_emoji = random.randint(0, 9) // 2
            if qq_or_emoji:
                return '[' + random.choice(list(qq_face.keys())) + ']'
            else:
                return EmojiCodeMap2[random.choice(list(EmojiCodeMap2.keys()))]
        except:
            pass


def parse_emoji_in_span(span):
    se = emoji_pattern.search(span)
    if se:
        return emoji_pattern.sub(get_emoji_by_code(se.group(1)), span)
    else:
        return span


def get_emoji_by_code(code):
    return EmojiCodeMap2.get(str(code), EmojiCodeMap.get(str(code), '<Emoji>'))

qq_face = {
    "微笑": "0",
    "撇嘴": "1",
    "色": "2",
    "发呆": "3",
    "得意": "4",
    "流泪": "5",
    "害羞": "6",
    "闭嘴": "7",
    "睡": "8",
    "大哭": "9",
    "尴尬": "10",
    "发怒": "11",
    "调皮": "12",
    "呲牙": "13",
    "惊讶": "14",
    "难过": "15",
    "酷": "16",
    "冷汗": "17",
    "抓狂": "18",
    "吐": "19",
    "偷笑": "20",
    "可爱": "21",
    "愉快": "21",
    "白眼": "22",
    "傲慢": "23",
    "饥饿": "24",
    "困": "25",
    "惊恐": "26",
    "流汗": "27",
    "憨笑": "28",
    "悠闲": "29",
    "大兵": "29",
    "奋斗": "30",
    "咒骂": "31",
    "疑问": "32",
    "嘘": "33",
    "晕": "34",
    "疯了": "35",
    "折磨": "35",
    "衰": "36",
    "骷髅": "37",
    "敲打": "38",
    "再见": "39",
    "擦汗": "40",
    "抠鼻": "41",
    "鼓掌": "42",
    "糗大了": "43",
    "坏笑": "44",
    "左哼哼": "45",
    "右哼哼": "46",
    "哈欠": "47",
    "鄙视": "48",
    "委屈": "49",
    "快哭了": "50",
    "阴险": "51",
    "亲亲": "52",
    "吓": "53",
    "可怜": "54",
    "菜刀": "55",
    "西瓜": "56",
    "啤酒": "57",
    "篮球": "58",
    "乒乓": "59",
    "咖啡": "60",
    "饭": "61",
    "猪头": "62",
    "玫瑰": "63",
    "凋谢": "64",
    "嘴唇": "65",
    "示爱": "65",
    "爱心": "66",
    "心碎": "67",
    "蛋糕": "68",
    "闪电": "69",
    "炸弹": "70",
    "刀": "71",
    "足球": "72",
    "瓢虫": "73",
    "便便": "74",
    "月亮": "75",
    "太阳": "76",
    "礼物": "77",
    "拥抱": "78",
    "强": "79",
    "弱": "80",
    "握手": "81",
    "胜利": "82",
    "抱拳": "83",
    "勾引": "84",
    "拳头": "85",
    "差劲": "86",
    "爱你": "87",
    "NO": "88",
    "OK": "89",
    "爱情": "90",
    "飞吻": "91",
    "跳跳": "92",
    "发抖": "93",
    "怄火": "94",
    "转圈": "95",
    "磕头": "96",
    "回头": "97",
    "跳绳": "98",
    "投降": "99",
    "激动": "100",
    "乱舞": "101",
    "献吻": "102",
    "左太极": "103",
    "右太极": "104",
    "Smile": "0",
    "Grimace": "1",
    "Drool": "2",
    "Scowl": "3",
    "Chill": "4",
    "CoolGuy": "4",
    "Sob": "5",
    "Shy": "6",
    "Shutup": "7",
    "Silent": "7",
    "Sleep": "8",
    "Cry": "9",
    "Awkward": "10",
    "Pout": "11",
    "Angry": "11",
    "Wink": "12",
    "Tongue": "12",
    "Grin": "13",
    "Surprised": "14",
    "Surprise": "14",
    "Frown": "15",
    "Cool": "16",
    "Ruthless": "16",
    "Tension": "17",
    "Blush": "17",
    "Scream": "18",
    "Crazy": "18",
    "Puke": "19",
    "Chuckle": "20",
    "Joyful": "21",
    "Slight": "22",
    "Smug": "23",
    "Hungry": "24",
    "Drowsy": "25",
    "Panic": "26",
    "Sweat": "27",
    "Laugh": "28",
    "Loafer": "29",
    "Commando": "29",
    "Strive": "30",
    "Determined": "30",
    "Scold": "31",
    "Doubt": "32",
    "Shocked": "32",
    "Shhh": "33",
    "Dizzy": "34",
    "Tormented": "35",
    "BadLuck": "36",
    "Toasted": "36",
    "Skull": "37",
    "Hammer": "38",
    "Wave": "39",
    "Relief": "40",
    "Speechless": "40",
    "DigNose": "41",
    "NosePick": "41",
    "Clap": "42",
    "Shame": "43",
    "Trick": "44",
    "Bah！L": "45",
    "Bah！R": "46",
    "Yawn": "47",
    "Lookdown": "48",
    "Pooh-pooh": "48",
    "Wronged": "49",
    "Shrunken": "49",
    "Puling": "50",
    "TearingUp": "50",
    "Sly": "51",
    "Kiss": "52",
    "Uh-oh": "53",
    "Wrath": "53",
    "Whimper": "54",
    "Cleaver": "55",
    "Melon": "56",
    "Watermelon": "56",
    "Beer": "57",
    "Basketball": "58",
    "PingPong": "59",
    "Coffee": "60",
    "Rice": "61",
    "Pig": "62",
    "Rose": "63",
    "Wilt": "64",
    "Lip": "65",
    "Lips": "65",
    "Heart": "66",
    "BrokenHeart": "67",
    "Cake": "68",
    "Lightning": "69",
    "Bomb": "70",
    "Dagger": "71",
    "Soccer": "72",
    "Ladybug": "73",
    "Poop": "74",
    "Moon": "75",
    "Sun": "76",
    "Gift": "77",
    "Hug": "78",
    "Strong": "79",
    "ThumbsUp": "79",
    "Weak": "80",
    "ThumbsDown": "80",
    "Shake": "81",
    "Victory": "82",
    "Peace": "82",
    "Admire": "83",
    "Fight": "83",
    "Beckon": "84",
    "Fist": "85",
    "Pinky": "86",
    "Love": "2",
    "RockOn": "87",
    "No": "88",
    "Nuh-uh": "88",
    "InLove": "90",
    "Blowkiss": "91",
    "Waddle": "92",
    "Tremble": "93",
    "Aaagh!": "94",
    "Twirl": "95",
    "Kotow": "96",
    "Lookback": "97",
    "Dramatic": "97",
    "Jump": "98",
    "JumpRope": "98",
    "Give-in": "99",
    "Surrender": "99",
    "Hooray": "100",
    "HeyHey": "101",
    "Meditate": "101",
    "Smooch": "102",
    "TaiJi L": "103",
    "TaiChi L": "103",
    "TaiJi R": "104",
    "TaiChi R": "104",
    "發呆": "3",
    "流淚": "5",
    "閉嘴": "7",
    "尷尬": "10",
    "發怒": "11",
    "調皮": "12",
    "驚訝": "14",
    "難過": "15",
    "饑餓": "24",
    "累": "25",
    "驚恐": "26",
    "悠閑": "29",
    "奮鬥": "30",
    "咒罵": "31",
    "疑問": "32",
    "噓": "33",
    "暈": "34",
    "瘋了": "35",
    "骷髏頭": "37",
    "再見": "39",
    "摳鼻": "41",
    "羞辱": "43",
    "壞笑": "44",
    "鄙視": "48",
    "陰險": "51",
    "親親": "52",
    "嚇": "53",
    "可憐": "54",
    "籃球": "58",
    "飯": "61",
    "豬頭": "62",
    "枯萎": "64",
    "愛心": "66",
    "閃電": "69",
    "炸彈": "70",
    "甲蟲": "73",
    "太陽": "76",
    "禮物": "77",
    "擁抱": "78",
    "強": "79",
    "勝利": "82",
    "拳頭": "85",
    "差勁": "86",
    "愛你": "88",
    "愛情": "90",
    "飛吻": "91",
    "發抖": "93",
    "噴火": "94",
    "轉圈": "95",
    "磕頭": "96",
    "回頭": "97",
    "跳繩": "98",
    "激動": "100",
    "亂舞": "101",
    "獻吻": "102",
    "左太極": "103",
    "右太極": "104",
}
emoji_face = {
    "<笑脸>": "1f604",
    "<笑臉>": "1f604",
    "<Laugh>": "1f604",
    "<开心>": "1f60a",
    "<開心>": "1f60a",
    "<Happy>": "1f60a",
    "<大笑>": "1f603",
    "<Big Smile>": "1f603",
    "<热情>": "263a",
    "<熱情>": "263a",
    "<Glowing>": "263a",
    "<眨眼>": "1f609",
    "<Wink>": "1f609",
    "<色>": "1f60d",
    "<Love>": "1f60d",
    "<Drool>": "1f60d",
    "<接吻>": "1f618",
    "<Smooch>": "1f618",
    "<亲吻>": "1f61a",
    "<親吻>": "1f61a",
    "<Kiss>": "1f61a",
    "<脸红>": "1f633",
    "<臉紅>": "1f633",
    "<Blush>": "1f633",
    "<露齿笑>": "1f63c",
    "<露齒笑>": "1f63c",
    "<Grin>": "1f63c",
    "<满意>": "1f60c",
    "<滿意>": "1f60c",
    "<Satisfied>": "1f60c",
    "<戏弄>": "1f61c",
    "<戲弄>": "1f61c",
    "<Tease>": "1f61c",
    "<吐舌>": "1f445",
    "<Tongue>": "1f445",
    "<无语>": "1f612",
    "<無語>": "1f612",
    "<Speechless>": "1f612",
    "<得意>": "1f60f",
    "<Smirk>": "1f60f",
    "<CoolGuy>": "1f60f",
    "<汗>": "1f613",
    "<Sweat>": "1f613",
    "<失望>": "1f640",
    "<Let Down>": "1f640",
    "<低落>": "1f61e",
    "<Low>": "1f61e",
    "<呸>": "1f616",
    "<Ugh>": "1f616",
    "<焦虑>": "1f625",
    "<焦慮>": "1f625",
    "<Anxious>": "1f625",
    "<担心>": "1f630",
    "<擔心>": "1f630",
    "<Worried>": "1f630",
    "<震惊>": "1f628",
    "<震驚>": "1f628",
    "<Shocked>": "1f628",
    "<悔恨>": "1f62b",
    "<D’oh!>": "1f62b",
    "<眼泪>": "1f622",
    "<眼淚>": "1f622",
    "<Tear>": "1f622",
    "<哭>": "1f62d",
    "<Cry>": "1f62d",
    "<破涕为笑>": "1f602",
    "<破涕為笑>": "1f602",
    "<Lol>": "1f602",
    "<晕>": "1f632",
    "<Dead>": "1f632",
    "<Dizzy>": "1f632",
    "<恐惧>": "1f631",
    "<恐懼>": "1f631",
    "<Terror>": "1f631",
    "<心烦>": "1f620",
    "<心煩>": "1f620",
    "<Upset>": "1f620",
    "<生气>": "1f63e",
    "<生氣>": "1f63e",
    "<Angry>": "1f63e",
    "<睡觉>": "1f62a",
    "<睡覺>": "1f62a",
    "<Zzz>": "1f62a",
    "<生病>": "1f637",
    "<Sick>": "1f637",
    "<恶魔>": "1f47f",
    "<惡魔>": "1f47f",
    "<Demon>": "1f47f",
    "<外星人>": "1f47d",
    "<Alien>": "1f47d",
    "<心>": "2764",
    "<Heart>": "2764",
    "<心碎>": "1f494",
    "<Heartbroken>": "1f494",
    "<BrokenHeart>": "1f494",
    "<丘比特>": "1f498",
    "<Cupid>": "1f498",
    "<闪烁>": "2728",
    "<閃爍>": "2728",
    "<Twinkle>": "2728",
    "<星星>": "1f31f",
    "<Star>": "1f31f",
    "<叹号>": "2755",
    "<嘆號>": "2755",
    "<!>": "2755",
    "<问号>": "2754",
    "<問號>": "2754",
    "<?>": "2754",
    "<睡着>": "1f4a4",
    "<睡著>": "1f4a4",
    "<Asleep>": "1f4a4",
    "<水滴>": "1f4a6",
    "<Drops>": "1f4a6",
    "<音乐>": "1f3b5",
    "<音樂>": "1f3b5",
    "<Music>": "1f3b5",
    "<火>": "1f525",
    "<Fire>": "1f525",
    "<便便>": "1f4a9",
    "<Poop>": "1f4a9",
    "<强>": "1f44d",
    "<強>": "1f44d",
    "<ThumbsUp>": "1f44d",
    "<弱>": "1f44e",
    "<ThumbsDown>": "1f44e",
    "<拳头>": "1f44a",
    "<拳頭>": "1f44a",
    "<Punch>": "1f44a",
    "<Fist>": "1f44a",
    "<胜利>": "270c",
    "<勝利>": "270c",
    "<Peace>": "270c",
    "<上>": "1f446",
    "<Up>": "1f446",
    "<下>": "1f447",
    "<Down>": "1f447",
    "<右>": "1f449",
    "<Right>": "1f449",
    "<左>": "1f448",
    "<Left>": "1f448",
    "<第一>": "261d",
    "<#1>": "261d",
    "<强壮>": "1f4aa",
    "<強壯>": "1f4aa",
    "<Strong>": "1f4aa",
    "<吻>": "1f48f",
    "<Kissing>": "1f48f",
    "<热恋>": "1f491",
    "<熱戀>": "1f491",
    "<Couple>": "1f491",
    "<男孩>": "1f466",
    "<Boy>": "1f466",
    "<女孩>": "1f467",
    "<Girl>": "1f467",
    "<女士>": "1f469",
    "<Lady>": "1f469",
    "<男士>": "1f468",
    "<Man>": "1f468",
    "<天使>": "1f47c",
    "<Angel>": "1f47c",
    "<骷髅>": "1f480",
    "<骷髏>": "1f480",
    "<Skull>": "1f480",
    "<红唇>": "1f48b",
    "<紅唇>": "1f48b",
    "<Lips>": "1f48b",
    "<太阳>": "2600",
    "<太陽>": "2600",
    "<Sun>": "2600",
    "<下雨>": "2614",
    "<Rain>": "2614",
    "<多云>": "2601",
    "<多雲>": "2601",
    "<Cloud>": "2601",
    "<雪人>": "26c4",
    "<Snowman>": "26c4",
    "<月亮>": "1f319",
    "<Moon>": "1f319",
    "<闪电>": "26a1",
    "<閃電>": "26a1",
    "<Lightning>": "26a1",
    "<海浪>": "1f30a",
    "<Waves>": "1f30a",
    "<猫>": "1f431",
    "<貓>": "1f431",
    "<Cat>": "1f431",
    "<小狗>": "1f429",
    "<Doggy>": "1f429",
    "<老鼠>": "1f42d",
    "<Mouse>": "1f42d",
    "<仓鼠>": "1f439",
    "<倉鼠>": "1f439",
    "<Hamster>": "1f439",
    "<兔子>": "1f430",
    "<Rabbit>": "1f430",
    "<狗>": "1f43a",
    "<Dog>": "1f43a",
    "<青蛙>": "1f438",
    "<Frog>": "1f438",
    "<老虎>": "1f42f",
    "<Tiger>": "1f42f",
    "<考拉>": "1f428",
    "<Koala>": "1f428",
    "<熊>": "1f43b",
    "<Bear>": "1f43b",
    "<猪>": "1f437",
    "<豬>": "1f437",
    "<Pig>": "1f437",
    "<牛>": "1f42e",
    "<Cow>": "1f42e",
    "<野猪>": "1f417",
    "<野豬>": "1f417",
    "<Boar>": "1f417",
    "<猴子>": "1f435",
    "<Monkey>": "1f435",
    "<马>": "1f434",
    "<馬>": "1f434",
    "<Horse>": "1f434",
    "<蛇>": "1f40d",
    "<Snake>": "1f40d",
    "<鸽子>": "1f426",
    "<鴿子>": "1f426",
    "<Pigeon>": "1f426",
    "<鸡>": "1f414",
    "<雞>": "1f414",
    "<Chicken>": "1f414",
    "<企鹅>": "1f427",
    "<企鵝>": "1f427",
    "<Penguin>": "1f427",
    "<毛虫>": "1f41b",
    "<毛蟲>": "1f41b",
    "<Caterpillar>": "1f41b",
    "<章鱼>": "1f419",
    "<八爪魚>": "1f419",
    "<Octopus>": "1f419",
    "<鱼>": "1f420",
    "<魚>": "1f420",
    "<Fish>": "1f420",
    "<鲸鱼>": "1f433",
    "<鯨魚>": "1f433",
    "<Whale>": "1f433",
    "<海豚>": "1f42c",
    "<Dolphin>": "1f42c",
    "<玫瑰>": "1f339",
    "<Rose>": "1f339",
    "<花>": "1f33a",
    "<Flower>": "1f33a",
    "<棕榈树>": "1f334",
    "<棕櫚樹>": "1f334",
    "<Palm>": "1f334",
    "<仙人掌>": "1f335",
    "<Cactus>": "1f335",
    "<礼盒>": "1f49d",
    "<禮盒>": "1f49d",
    "<Candy Box>": "1f49d",
    "<南瓜灯>": "1f383",
    "<南瓜燈>": "1f383",
    "<Jack-o-lantern>": "1f383",
    "<鬼魂>": "1f47b",
    "<Ghost>": "1f47b",
    "<圣诞老人>": "1f385",
    "<聖誕老人>": "1f385",
    "<Santa>": "1f385",
    "<圣诞树>": "1f384",
    "<聖誕樹>": "1f384",
    "<Xmas Tree>": "1f384",
    "<礼物>": "1f381",
    "<禮物>": "1f381",
    "<Gift>": "1f381",
    "<铃>": "1f514",
    "<鈴鐺>": "1f514",
    "<Bell>": "1f514",
    "<庆祝>": "1f389",
    "<慶祝>": "1f389",
    "<Party>": "1f389",
    "<气球>": "1f388",
    "<氣球>": "1f388",
    "<Balloon>": "1f388",
    "<CD>": "1f4bf",
    "<相机>": "1f4f7",
    "<相機>": "1f4f7",
    "<Camera>": "1f4f7",
    "<录像机>": "1f3a5",
    "<錄影機>": "1f3a5",
    "<Film Camera>": "1f3a5",
    "<电脑>": "1f4bb",
    "<電腦>": "1f4bb",
    "<Computer>": "1f4bb",
    "<电视>": "1f4fa",
    "<電視>": "1f4fa",
    "<TV>": "1f4fa",
    "<电话>": "1f4de",
    "<電話>": "1f4de",
    "<Phone>": "1f4de",
    "<解锁>": "1f513",
    "<解鎖>": "1f513",
    "<Unlocked>": "1f513",
    "<锁>": "1f512",
    "<鎖>": "1f512",
    "<Locked>": "1f512",
    "<钥匙>": "1f511",
    "<鑰匙>": "1f511",
    "<Key>": "1f511",
    "<成交>": "1f528",
    "<Judgement>": "1f528",
    "<灯泡>": "1f4a1",
    "<燈泡>": "1f4a1",
    "<Light bulb>": "1f4a1",
    "<邮箱>": "1f4eb",
    "<郵箱>": "1f4eb",
    "<Mail>": "1f4eb",
    "<浴缸>": "1f6c0",
    "<Wash>": "1f6c0",
    "<钱>": "1f4b2",
    "<錢>": "1f4b2",
    "<Money>": "1f4b2",
    "<炸弹>": "1f4a3",
    "<炸彈>": "1f4a3",
    "<Bomb>": "1f4a3",
    "<手枪>": "1f52b",
    "<手槍>": "1f52b",
    "<Pistol>": "1f52b",
    "<药丸>": "1f48a",
    "<藥丸>": "1f48a",
    "<Pill>": "1f48a",
    "<橄榄球>": "1f3c8",
    "<橄欖球>": "1f3c8",
    "<Football>": "1f3c8",
    "<篮球>": "1f3c0",
    "<籃球>": "1f3c0",
    "<Basketball>": "1f3c0",
    "<足球>": "26bd",
    "<Soccer Ball>": "26bd",
    "<Soccer>": "26bd",
    "<棒球>": "26be",
    "<Baseball>": "26be",
    "<高尔夫>": "26f3",
    "<高爾夫>": "26f3",
    "<Golf>": "26f3",
    "<奖杯>": "1f3c6",
    "<獎盃>": "1f3c6",
    "<Trophy>": "1f3c6",
    "<入侵者>": "1f47e",
    "<Invader>": "1f47e",
    "<唱歌>": "1f3a4",
    "<Singing>": "1f3a4",
    "<吉他>": "1f3b8",
    "<Guitar>": "1f3b8",
    "<比基尼>": "1f459",
    "<Bikini>": "1f459",
    "<皇冠>": "1f451",
    "<Crown>": "1f451",
    "<雨伞>": "1f302",
    "<雨傘>": "1f302",
    "<Umbrella>": "1f302",
    "<手提包>": "1f45c",
    "<Purse>": "1f45c",
    "<口红>": "1f484",
    "<Lipstick>": "1f484",
    "<戒指>": "1f48d",
    "<Ring>": "1f48d",
    "<钻石>": "1f48e",
    "<鑽石>": "1f48e",
    "<Gem>": "1f48e",
    "<咖啡>": "2615",
    "<Coffee>": "2615",
    "<啤酒>": "1f37a",
    "<Beer>": "1f37a",
    "<干杯>": "1f37b",
    "<乾杯>": "1f37b",
    "<Toast>": "1f37b",
    "<鸡尾酒>": "1f377",
    "<雞尾酒>": "1f377",
    "<Martini>": "1f377",
    "<汉堡>": "1f354",
    "<漢堡>": "1f354",
    "<Burger>": "1f354",
    "<薯条>": "1f35f",
    "<薯條>": "1f35f",
    "<Fries>": "1f35f",
    "<意面>": "1f35d",
    "<意粉>": "1f35d",
    "<Sphaghetti>": "1f35d",
    "<寿司>": "1f363",
    "<壽司>": "1f363",
    "<Sushi>": "1f363",
    "<面条>": "1f35c",
    "<麵條>": "1f35c",
    "<Noodles>": "1f35c",
    "<煎蛋>": "1f373",
    "<Eggs>": "1f373",
    "<冰激凌>": "1f366",
    "<雪糕>": "1f366",
    "<Ice Cream>": "1f366",
    "<蛋糕>": "1f382",
    "<Cake>": "1f382",
    "<苹果>": "1f34f",
    "<蘋果>": "1f34f",
    "<Apple>": "1f34f",
    "<飞机>": "2708",
    "<飛機>": "2708",
    "<Plane>": "2708",
    "<火箭>": "1f680",
    "<Rocket ship>": "1f680",
    "<自行车>": "1f6b2",
    "<單車>": "1f6b2",
    "<Bike>": "1f6b2",
    "<高铁>": "1f684",
    "<高鐵>": "1f684",
    "<Bullet Train>": "1f684",
    "<警告>": "26a0",
    "<Warning>": "26a0",
    "<旗>": "1f3c1",
    "<Flag>": "1f3c1",
    "<男人>": "1f6b9",
    "<男>": "1f6b9",
    "<Men>": "1f6b9",
    "<女人>": "1f6ba",
    "<女>": "1f6ba",
    "<Women>": "1f6ba",
    "<O>": "2b55",
    "<X>": "274e",
    "<版权>": "a9",
    "<版權>": "a9",
    "<Copyright>": "a9",
    "<注册商标>": "ae",
    "<注冊商標>": "ae",
    "<Registered TM>": "ae",
    "<商标>": "2122",
    "<商標>": "2122",
    "<Trademark>": "2122",
}

EmojiCodeMap = {
    "1f604": "",
    "1f60a": "",
    "1f603": "",
    "263a": "",
    "1f609": "",
    "1f60d": "",
    "1f618": "",
    "1f61a": "",
    "1f633": "",
    "1f63c": "",
    "1f60c": "",
    "1f61c": "",
    "1f445": "",
    "1f612": "",
    "1f60f": "",
    "1f613": "",
    "1f640": "",
    "1f61e": "",
    "1f616": "",
    "1f625": "",
    "1f630": "",
    "1f628": "",
    "1f62b": "",
    "1f622": "",
    "1f62d": "",
    "1f602": "",
    "1f632": "",
    "1f631": "",
    "1f620": "",
    "1f63e": "",
    "1f62a": "",
    "1f637": "",
    "1f47f": "",
    "1f47d": "",
    "2764": "",
    "1f494": "",
    "1f498": "",
    "2728": "",
    "1f31f": "",
    "2755": "",
    "2754": "",
    "1f4a4": "",
    "1f4a6": "",
    "1f3b5": "",
    "1f525": "",
    "1f4a9": "",
    "1f44d": "",
    "1f44e": "",
    "1f44a": "",
    "270c": "",
    "1f446": "",
    "1f447": "",
    "1f449": "",
    "1f448": "",
    "261d": "",
    "1f4aa": "",
    "1f48f": "",
    "1f491": "",
    "1f466": "",
    "1f467": "",
    "1f469": "",
    "1f468": "",
    "1f47c": "",
    "1f480": "",
    "1f48b": "",
    "2600": "",
    "2614": "",
    "2601": "",
    "26c4": "",
    "1f319": "",
    "26a1": "",
    "1f30a": "",
    "1f431": "",
    "1f429": "",
    "1f42d": "",
    "1f439": "",
    "1f430": "",
    "1f43a": "",
    "1f438": "",
    "1f42f": "",
    "1f428": "",
    "1f43b": "",
    "1f437": "",
    "1f42e": "",
    "1f417": "",
    "1f435": "",
    "1f434": "",
    "1f40d": "",
    "1f426": "",
    "1f414": "",
    "1f427": "",
    "1f41b": "",
    "1f419": "",
    "1f420": "",
    "1f433": "",
    "1f42c": "",
    "1f339": "",
    "1f33a": "",
    "1f334": "",
    "1f335": "",
    "1f49d": "",
    "1f383": "",
    "1f47b": "",
    "1f385": "",
    "1f384": "",
    "1f381": "",
    "1f514": "",
    "1f389": "",
    "1f388": "",
    "1f4bf": "",
    "1f4f7": "",
    "1f3a5": "",
    "1f4bb": "",
    "1f4fa": "",
    "1f4de": "",
    "1f513": "",
    "1f512": "",
    "1f511": "",
    "1f528": "",
    "1f4a1": "",
    "1f4eb": "",
    "1f6c0": "",
    "1f4b2": "",
    "1f4a3": "",
    "1f52b": "",
    "1f48a": "",
    "1f3c8": "",
    "1f3c0": "",
    "26bd": "",
    "26be": "",
    "26f3": "",
    "1f3c6": "",
    "1f47e": "",
    "1f3a4": "",
    "1f3b8": "",
    "1f459": "",
    "1f451": "",
    "1f302": "",
    "1f45c": "",
    "1f484": "",
    "1f48d": "",
    "1f48e": "",
    "2615": "",
    "1f37a": "",
    "1f37b": "",
    "1f377": "",
    "1f354": "",
    "1f35f": "",
    "1f35d": "",
    "1f363": "",
    "1f35c": "",
    "1f373": "",
    "1f366": "",
    "1f382": "",
    "1f34f": "",
    "2708": "",
    "1f680": "",
    "1f6b2": "",
    "1f684": "",
    "26a0": "",
    "1f3c1": "",
    "1f6b9": "",
    "1f6ba": "",
    "2b55": "",
    "274e": "",
    "a9": "",
    "ae": "",
    "2122": "",
}

EmojiCodeMap2 = {
    "2708": "✈",  # airplane
    "23f0": "⏰",  # alarm clock
    "1f47e": "👾",  # alien monster
    "1f691": "🚑",  # ambulance
    "1f3c8": "🏈",  # american football
    "2693": "⚓",  # anchor
    "1f4a2": "💢",  # anger symbol
    "1f620": "😠",  # angry face
    "1f41c": "🐜",  # ant
    "1f4f6": "📶",  # antenna with bars
    "2652": "♒",  # aquarius
    "2648": "♈",  # aries
    "2935": "⤵",  # arrow pointing rightwards then curving downwards
    "2934": "⤴",  # arrow pointing rightwards then curving upwards
    "1f3a8": "🎨",  # artist palette
    "1f632": "😲",  # astonished face
    "1f45f": "👟",  # athletic shoe
    "1f346": "🍆",  # aubergine
    "1f3e7": "🏧",  # automated teller machine
    "1f697": "🚗",  # automobile
    "1f476": "👶",  # baby
    "1f47c": "👼",  # baby angel
    "1f424": "🐤",  # baby chick
    "1f6bc": "🚼",  # baby symbol
    "1f519": "🔙",  # back with leftwards arrow above
    "1f42b": "🐫",  # bactrian camel
    "1f388": "🎈",  # balloon
    "2611": "☑",  # ballot box with check
    "1f34c": "🍌",  # banana
    "1f3e6": "🏦",  # bank
    "1f4b5": "💵",  # banknote with dollar sign
    "1f4b4": "💴",  # banknote with yen sign
    "1f4ca": "📊",  # bar chart
    "1f488": "💈",  # barber pole
    "26be": "⚾",  # baseball
    "1f3c0": "🏀",  # basketball and hoop
    "1f6c0": "🛀",  # bath
    "1f50b": "🔋",  # battery
    "1f43b": "🐻",  # bear face
    "1f493": "💓",  # beating heart
    "1f37a": "🍺",  # beer mug
    "1f514": "🔔",  # bell
    "1f371": "🍱",  # bento box
    "1f6b2": "🚲",  # bicycle
    "1f459": "👙",  # bikini
    "1f3b1": "🎱",  # billiards
    "1f426": "🐦",  # bird
    "1f382": "🎂",  # birthday cake
    "2663": "♣",  # black club suit
    "2666": "♦",  # black diamond suit
    "23ec": "⏬",  # black down-pointing double triangle
    "2665": "♥",  # black heart suit
    "2b1b": "⬛",  # black large square
    "23ea": "⏪",  # black left-pointing double triangle
    "25c0": "◀",  # black left-pointing triangle
    "25fe": "◾",  # black medium small square
    "25fc": "◼",  # black medium square
    "2712": "✒",  # black nib
    "2753": "❓",  # black question mark ornament
    "23e9": "⏩",  # black right-pointing double triangle
    "25b6": "▶",  # black right-pointing triangle
    "27a1": "➡",  # black rightwards arrow
    "2702": "✂",  # black scissors
    "25aa": "▪",  # black small square
    "2660": "♠",  # black spade suit
    "1f532": "🔲",  # black square button
    "2600": "☀",  # black sun with rays
    "260e": "☎",  # black telephone
    "267b": "♻",  # black universal recycling symbol
    "23eb": "⏫",  # black up-pointing double triangle
    "1f33c": "🌼",  # blossom
    "1f421": "🐡",  # blowfish
    "1f4d8": "📘",  # blue book
    "1f499": "💙",  # blue heart
    "1f417": "🐗",  # boar
    "1f4a3": "💣",  # bomb
    "1f516": "🔖",  # bookmark
    "1f4d1": "📑",  # bookmark tabs
    "1f4da": "📚",  # books
    "1f490": "💐",  # bouquet
    "1f3b3": "🎳",  # bowling
    "1f466": "👦",  # boy
    "1f35e": "🍞",  # bread
    "1f470": "👰",  # bride with veil
    "1f309": "🌉",  # bridge at night
    "1f4bc": "💼",  # briefcase
    "1f494": "💔",  # broken heart
    "1f41b": "🐛",  # bug
    "1f68c": "🚌",  # bus
    "1f68f": "🚏",  # bus stop
    "1f464": "👤",  # bust in silhouette
    "1f335": "🌵",  # cactus
    "1f4c5": "📅",  # calendar
    "1f4f7": "📷",  # camera
    "264b": "♋",  # cancer
    "1f36c": "🍬",  # candy
    "2651": "♑",  # capricorn
    "1f4c7": "📇",  # card index
    "1f3a0": "🎠",  # carousel horse
    "1f38f": "🎏",  # carp streamer
    "1f431": "🐱",  # cat face
    "1f639": "😹",  # cat face with tears of joy
    "1f63c": "😼",  # cat face with wry smile
    "1f4c9": "📉",  # chart with downwards trend
    "1f4c8": "📈",  # chart with upwards trend
    "1f4b9": "💹",  # chart with upwards trend and yen sign
    "1f4e3": "📣",  # cheering megaphone
    "1f3c1": "🏁",  # chequered flag
    "1f352": "🍒",  # cherries
    "1f338": "🌸",  # cherry blossom
    "1f330": "🌰",  # chestnut
    "1f414": "🐔",  # chicken
    "1f36b": "🍫",  # chocolate bar
    "1f384": "🎄",  # christmas tree
    "26ea": "⛪",  # church
    "1f3a6": "🎦",  # cinema
    "1f251": "🉑",  # circled ideograph accept
    "1f250": "🉐",  # circled ideograph advantage
    "3297": "㊗",  # circled ideograph congratulation
    "3299": "㊙",  # circled ideograph secret
    "24c2": "ⓜ",  # circled latin capital letter m
    "1f3aa": "🎪",  # circus tent
    "1f306": "🌆",  # cityscape at dusk
    "1f3ac": "🎬",  # clapper board
    "1f44f": "👏",  # clapping hands sign
    "1f37b": "🍻",  # clinking beer mugs
    "1f4cb": "📋",  # clipboard
    "1f557": "🕗",  # clock face eight oclock
    "1f55a": "🕚",  # clock face eleven oclock
    "1f554": "🕔",  # clock face five oclock
    "1f553": "🕓",  # clock face four oclock
    "1f558": "🕘",  # clock face nine oclock
    "1f550": "🕐",  # clock face one oclock
    "1f556": "🕖",  # clock face seven oclock
    "1f555": "🕕",  # clock face six oclock
    "1f559": "🕙",  # clock face ten oclock
    "1f552": "🕒",  # clock face three oclock
    "1f55b": "🕛",  # clock face twelve oclock
    "1f551": "🕑",  # clock face two oclock
    "1f503": "🔃",  # clockwise downwards and upwards open circle arrows
    "1f4d5": "📕",  # closed book
    "1f510": "🔐",  # closed lock with key
    "1f4ea": "📪",  # closed mailbox with lowered flag
    "1f4eb": "📫",  # closed mailbox with raised flag
    "1f302": "🌂",  # closed umbrella
    "2601": "☁",  # cloud
    "1f378": "🍸",  # cocktail glass
    "1f4a5": "💥",  # collision symbol
    "1f38a": "🎊",  # confetti ball
    "1f616": "😖",  # confounded face
    "1f6a7": "🚧",  # construction sign
    "1f477": "👷",  # construction worker
    "1f3ea": "🏪",  # convenience store
    "1f35a": "🍚",  # cooked rice
    "1f36a": "🍪",  # cookie
    "1f373": "🍳",  # cooking
    "00a9": "©",  # copyright sign
    "1f491": "💑",  # couple with heart
    "1f42e": "🐮",  # cow face
    "1f4b3": "💳",  # credit card
    "1f319": "🌙",  # crescent moon
    "274c": "❌",  # cross mark
    "1f38c": "🎌",  # crossed flags
    "1f451": "👑",  # crown
    "1f63f": "😿",  # crying cat face
    "1f622": "😢",  # crying face
    "1f52e": "🔮",  # crystal ball
    "27b0": "➰",  # curly loop
    "1f4b1": "💱",  # currency exchange
    "1f35b": "🍛",  # curry and rice
    "1f36e": "🍮",  # custard
    "1f300": "🌀",  # cyclone
    "1f483": "💃",  # dancer
    "1f361": "🍡",  # dango
    "1f4a8": "💨",  # dash symbol
    "1f69a": "🚚",  # delivery truck
    "1f3ec": "🏬",  # department store
    "1f4a0": "💠",  # diamond shape with a dot inside
    "1f3af": "🎯",  # direct hit
    "1f625": "😥",  # disappointed but relieved face
    "1f61e": "😞",  # disappointed face
    "1f635": "😵",  # dizzy face
    "1f4ab": "💫",  # dizzy symbol
    "1f436": "🐶",  # dog face
    "1f42c": "🐬",  # dolphin
    "1f6aa": "🚪",  # door
    "203c": "‼",  # double exclamation mark
    "1f369": "🍩",  # doughnut
    "1f53b": "🔻",  # down-pointing red triangle
    "1f53d": "🔽",  # down-pointing small red triangle
    "2b07": "⬇",  # downwards black arrow
    "1f432": "🐲",  # dragon face
    "1f457": "👗",  # dress
    "1f4a7": "💧",  # droplet
    "1f4c0": "📀",  # dvd
    "1f4e7": "📧",  # e-mail symbol
    "1f442": "👂",  # ear
    "1f33d": "🌽",  # ear of maize
    "1f33e": "🌾",  # ear of rice
    "1f30f": "🌏",  # earth globe asia-australia
    "2734": "✴",  # eight pointed black star
    "2733": "✳",  # eight spoked asterisk
    "1f4a1": "💡",  # electric light bulb
    "1f50c": "🔌",  # electric plug
    "1f526": "🔦",  # electric torch
    "1f418": "🐘",  # elephant
    "1f51a": "🔚",  # end with leftwards arrow above
    "2709": "✉",  # envelope
    "1f4e9": "📩",  # envelope with downwards arrow above
    "1f3f0": "🏰",  # european castle
    "2049": "⁉",  # exclamation question mark
    "1f47d": "👽",  # extraterrestrial alien
    "1f453": "👓",  # eyeglasses
    "1f440": "👀",  # eyes
    "1f486": "💆",  # face massage
    "1f60b": "😋",  # face savouring delicious food
    "1f631": "😱",  # face screaming in fear
    "1f618": "😘",  # face throwing a kiss
    "1f613": "😓",  # face with cold sweat
    "1f624": "😤",  # face with look of triumph
    "1f637": "😷",  # face with medical mask
    "1f645": "🙅",  # face with no good gesture
    "1f646": "🙆",  # face with ok gesture
    "1f630": "😰",  # face with open mouth and cold sweat
    "1f61d": "😝",  # face with stuck-out tongue and tightly-closed eyes
    "1f61c": "😜",  # face with stuck-out tongue and winking eye
    "1f602": "😂",  # face with tears of joy
    "1f3ed": "🏭",  # factory
    "1f342": "🍂",  # fallen leaf
    "1f46a": "👪",  # family
    "1f385": "🎅",  # father christmas
    "1f4e0": "📠",  # fax machine
    "1f628": "😨",  # fearful face
    "1f3a1": "🎡",  # ferris wheel
    "1f4c1": "📁",  # file folder
    "1f525": "🔥",  # fire
    "1f692": "🚒",  # fire engine
    "1f387": "🎇",  # firework sparkler
    "1f386": "🎆",  # fireworks
    "1f313": "🌓",  # first quarter moon symbol
    "1f31b": "🌛",  # first quarter moon with face
    "1f41f": "🐟",  # fish
    "1f365": "🍥",  # fish cake with swirl design
    "1f3a3": "🎣",  # fishing pole and fish
    "1f44a": "👊",  # fisted hand sign
    "26f3": "⛳",  # flag in hole
    "1f4aa": "💪",  # flexed biceps
    "1f4be": "💾",  # floppy disk
    "1f3b4": "🎴",  # flower playing cards
    "1f633": "😳",  # flushed face
    "1f301": "🌁",  # foggy
    "1f463": "👣",  # footprints
    "1f374": "🍴",  # fork and knife
    "26f2": "⛲",  # fountain
    "1f340": "🍀",  # four leaf clover
    "1f35f": "🍟",  # french fries
    "1f364": "🍤",  # fried shrimp
    "1f438": "🐸",  # frog face
    "1f425": "🐥",  # front-facing baby chick
    "26fd": "⛽",  # fuel pump
    "1f315": "🌕",  # full moon symbol
    "1f3b2": "🎲",  # game die
    "1f48e": "💎",  # gem stone
    "264a": "♊",  # gemini
    "1f47b": "👻",  # ghost
    "1f467": "👧",  # girl
    "1f31f": "🌟",  # glowing star
    "1f393": "🎓",  # graduation cap
    "1f347": "🍇",  # grapes
    "1f34f": "🍏",  # green apple
    "1f4d7": "📗",  # green book
    "1f49a": "💚",  # green heart
    "1f638": "😸",  # grinning cat face with smiling eyes
    "1f601": "😁",  # grinning face with smiling eyes
    "1f497": "💗",  # growing heart
    "1f482": "💂",  # guardsman
    "1f3b8": "🎸",  # guitar
    "1f487": "💇",  # haircut
    "1f354": "🍔",  # hamburger
    "1f528": "🔨",  # hammer
    "1f439": "🐹",  # hamster face
    "1f45c": "👜",  # handbag
    "1f64b": "🙋",  # happy person raising one hand
    "1f423": "🐣",  # hatching chick
    "1f3a7": "🎧",  # headphone
    "1f649": "🙉",  # hear-no-evil monkey
    "1f49f": "💟",  # heart decoration
    "1f498": "💘",  # heart with arrow
    "1f49d": "💝",  # heart with ribbon
    "2764": "❤",  # heavy black heart
    "2714": "✔",  # heavy check mark
    "2797": "➗",  # heavy division sign
    "1f4b2": "💲",  # heavy dollar sign
    "2757": "❗",  # heavy exclamation mark symbol
    "2b55": "⭕",  # heavy large circle
    "2796": "➖",  # heavy minus sign
    "2716": "✖",  # heavy multiplication x
    "2795": "➕",  # heavy plus sign
    "1f33f": "🌿",  # herb
    "1f33a": "🌺",  # hibiscus
    "26a1": "⚡",  # high voltage sign
    "1f460": "👠",  # high-heeled shoe
    "1f684": "🚄",  # high-speed train
    "1f685": "🚅",  # high-speed train with bullet nose
    "1f52a": "🔪",  # hocho
    "1f36f": "🍯",  # honey pot
    "1f41d": "🐝",  # honeybee
    "1f6a5": "🚥",  # horizontal traffic light
    "1f40e": "🐎",  # horse
    "1f434": "🐴",  # horse face
    "1f3e5": "🏥",  # hospital
    "2615": "☕",  # hot beverage
    "2668": "♨",  # hot springs
    "1f3e8": "🏨",  # hotel
    "231b": "⌛",  # hourglass
    "23f3": "⏳",  # hourglass with flowing sand
    "1f3e0": "🏠",  # house building
    "1f3e1": "🏡",  # house with garden
    "1f4af": "💯",  # hundred points symbol
    "1f368": "🍨",  # ice cream
    "1f47f": "👿",  # imp
    "1f4e5": "📥",  # inbox tray
    "1f4e8": "📨",  # incoming envelope
    "1f481": "💁",  # information desk person
    "2139": "ℹ",  # information source
    "1f520": "🔠",  # input symbol for latin capital letters
    "1f524": "🔤",  # input symbol for latin letters
    "1f521": "🔡",  # input symbol for latin small letters
    "1f522": "🔢",  # input symbol for numbers
    "1f523": "🔣",  # input symbol for symbols
    "1f3ee": "🏮",  # izakaya lantern
    "1f383": "🎃",  # jack-o-lantern
    "1f3ef": "🏯",  # japanese castle
    "1f38e": "🎎",  # japanese dolls
    "1f47a": "👺",  # japanese goblin
    "1f479": "👹",  # japanese ogre
    "1f3e3": "🏣",  # japanese post office
    "1f530": "🔰",  # japanese symbol for beginner
    "1f456": "👖",  # jeans
    "1f511": "🔑",  # key
    "1f51f": "🔟",  # keycap ten
    "1f458": "👘",  # kimono
    "1f48f": "💏",  # kiss
    "1f48b": "💋",  # kiss mark
    "1f63d": "😽",  # kissing cat face with closed eyes
    "1f61a": "😚",  # kissing face with closed eyes
    "1f428": "🐨",  # koala
    "1f41e": "🐞",  # lady beetle
    "1f535": "🔵",  # large blue circle
    "1f537": "🔷",  # large blue diamond
    "1f536": "🔶",  # large orange diamond
    "1f534": "🔴",  # large red circle
    "1f343": "🍃",  # leaf fluttering in wind
    "1f4d2": "📒",  # ledger
    "2194": "↔",  # left right arrow
    "1f50d": "🔍",  # left-pointing magnifying glass
    "21a9": "↩",  # leftwards arrow with hook
    "2b05": "⬅",  # leftwards black arrow
    "264c": "♌",  # leo
    "264e": "♎",  # libra
    "1f517": "🔗",  # link symbol
    "1f484": "💄",  # lipstick
    "1f512": "🔒",  # lock
    "1f50f": "🔏",  # lock with ink pen
    "1f36d": "🍭",  # lollipop
    "1f62d": "😭",  # loudly crying face
    "1f3e9": "🏩",  # love hotel
    "1f48c": "💌",  # love letter
    "1f004": "🀄",  # mahjong tile red dragon
    "1f468": "👨",  # man
    "1f46b": "👫",  # man and woman holding hands
    "1f472": "👲",  # man with gua pi mao
    "1f473": "👳",  # man with turban
    "1f45e": "👞",  # mans shoe
    "1f341": "🍁",  # maple leaf
    "1f356": "🍖",  # meat on bone
    "26ab": "⚫",  # medium black circle
    "26aa": "⚪",  # medium white circle
    "1f348": "🍈",  # melon
    "1f4dd": "📝",  # memo
    "1f6b9": "🚹",  # mens symbol
    "1f687": "🚇",  # metro
    "1f3a4": "🎤",  # microphone
    "1f30c": "🌌",  # milky way
    "1f4bd": "💽",  # minidisc
    "1f4f1": "📱",  # mobile phone
    "1f4f4": "📴",  # mobile phone off
    "1f4f2": "📲",  # mobile phone with rightwards arrow at left
    "1f4b0": "💰",  # money bag
    "1f4b8": "💸",  # money with wings
    "1f412": "🐒",  # monkey
    "1f435": "🐵",  # monkey face
    "1f391": "🎑",  # moon viewing ceremony
    "1f5fb": "🗻",  # mount fuji
    "1f42d": "🐭",  # mouse face
    "1f444": "👄",  # mouth
    "1f3a5": "🎥",  # movie camera
    "1f5ff": "🗿",  # moyai
    "1f3b6": "🎶",  # multiple musical notes
    "1f344": "🍄",  # mushroom
    "1f3b9": "🎹",  # musical keyboard
    "1f3b5": "🎵",  # musical note
    "1f3bc": "🎼",  # musical score
    "1f485": "💅",  # nail polish
    "1f4db": "📛",  # name badge
    "1f454": "👔",  # necktie
    "1f18e": "🆎",  # negative squared ab
    "274e": "❎",  # negative squared cross mark
    "1f170": "🅰",  # negative squared latin capital letter a
    "1f171": "🅱",  # negative squared latin capital letter b
    "1f17e": "🅾",  # negative squared latin capital letter o
    "1f17f": "🅿",  # negative squared latin capital letter p
    "1f311": "🌑",  # new moon symbol
    "1f4f0": "📰",  # newspaper
    "1f303": "🌃",  # night with stars
    "26d4": "⛔",  # no entry
    "1f6ab": "🚫",  # no entry sign
    "1f51e": "🔞",  # no one under eighteen symbol
    "1f6ad": "🚭",  # no smoking symbol
    "2197": "↗",  # north east arrow
    "2196": "↖",  # north west arrow
    "1f443": "👃",  # nose
    "1f4d3": "📓",  # notebook
    "1f4d4": "📔",  # notebook with decorative cover
    "1f529": "🔩",  # nut and bolt
    "1f419": "🐙",  # octopus
    "1f362": "🍢",  # oden
    "1f3e2": "🏢",  # office building
    "1f44c": "👌",  # ok hand sign
    "1f474": "👴",  # older man
    "1f475": "👵",  # older woman
    "1f51b": "🔛",  # on with exclamation mark with left right arrow above
    "1f4d6": "📖",  # open book
    "1f4c2": "📂",  # open file folder
    "1f450": "👐",  # open hands sign
    "1f513": "🔓",  # open lock
    "26ce": "⛎",  # ophiuchus
    "1f4bf": "💿",  # optical disc
    "1f4d9": "📙",  # orange book
    "1f4e4": "📤",  # outbox tray
    "1f4e6": "📦",  # package
    "1f4c4": "📄",  # page facing up
    "1f4c3": "📃",  # page with curl
    "1f4df": "📟",  # pager
    "1f334": "🌴",  # palm tree
    "1f43c": "🐼",  # panda face
    "1f4ce": "📎",  # paperclip
    "303d": "〽",  # part alternation mark
    "1f389": "🎉",  # party popper
    "1f43e": "🐾",  # paw prints
    "1f351": "🍑",  # peach
    "1f6b6": "🚶",  # pedestrian
    "270f": "✏",  # pencil
    "1f427": "🐧",  # penguin
    "1f614": "😔",  # pensive face
    "1f3ad": "🎭",  # performing arts
    "1f623": "😣",  # persevering face
    "1f647": "🙇",  # person bowing deeply
    "1f64d": "🙍",  # person frowning
    "1f64c": "🙌",  # person raising both hands in celebration
    "1f471": "👱",  # person with blond hair
    "1f64f": "🙏",  # person with folded hands
    "1f64e": "🙎",  # person with pouting face
    "1f4bb": "💻",  # personal computer
    "1f437": "🐷",  # pig face
    "1f43d": "🐽",  # pig nose
    "1f4a9": "💩",  # pile of poo
    "1f48a": "💊",  # pill
    "1f38d": "🎍",  # pine decoration
    "1f34d": "🍍",  # pineapple
    "2653": "♓",  # pisces
    "1f52b": "🔫",  # pistol
    "1f0cf": "🃏",  # playing card black joker
    "1f693": "🚓",  # police car
    "1f6a8": "🚨",  # police cars revolving light
    "1f46e": "👮",  # police officer
    "1f429": "🐩",  # poodle
    "1f4ee": "📮",  # postbox
    "1f372": "🍲",  # pot of food
    "1f45d": "👝",  # pouch
    "1f357": "🍗",  # poultry leg
    "1f63e": "😾",  # pouting cat face
    "1f621": "😡",  # pouting face
    "1f478": "👸",  # princess
    "1f4e2": "📢",  # public address loudspeaker
    "1f49c": "💜",  # purple heart
    "1f45b": "👛",  # purse
    "1f4cc": "📌",  # pushpin
    "1f430": "🐰",  # rabbit face
    "1f4fb": "📻",  # radio
    "1f518": "🔘",  # radio button
    "1f683": "🚃",  # railway car
    "1f308": "🌈",  # rainbow
    "270a": "✊",  # raised fist
    "270b": "✋",  # raised hand
    "1f699": "🚙",  # recreational vehicle
    "1f34e": "🍎",  # red apple
    "00ae": "®",  # registered sign
    "1f60c": "😌",  # relieved face
    "1f6bb": "🚻",  # restroom
    "1f49e": "💞",  # revolving hearts
    "1f380": "🎀",  # ribbon
    "1f359": "🍙",  # rice ball
    "1f358": "🍘",  # rice cracker
    "1f50e": "🔎",  # right-pointing magnifying glass
    "21aa": "↪",  # rightwards arrow with hook
    "1f48d": "💍",  # ring
    "1f360": "🍠",  # roasted sweet potato
    "1f680": "🚀",  # rocket
    "1f3a2": "🎢",  # roller coaster
    "1f339": "🌹",  # rose
    "1f4cd": "📍",  # round pushpin
    "1f3c3": "🏃",  # runner
    "1f3bd": "🎽",  # running shirt with sash
    "2650": "♐",  # sagittarius
    "26f5": "⛵",  # sailboat
    "1f376": "🍶",  # sake bottle and cup
    "1f4e1": "📡",  # satellite antenna
    "1f3b7": "🎷",  # saxophone
    "1f3eb": "🏫",  # school
    "1f392": "🎒",  # school satchel
    "264f": "♏",  # scorpius
    "1f4dc": "📜",  # scroll
    "1f4ba": "💺",  # seat
    "1f648": "🙈",  # see-no-evil monkey
    "1f331": "🌱",  # seedling
    "1f367": "🍧",  # shaved ice
    "1f411": "🐑",  # sheep
    "1f6a2": "🚢",  # ship
    "1f320": "🌠",  # shooting star
    "1f370": "🍰",  # shortcake
    "1f5fe": "🗾",  # silhouette of japan
    "1f52f": "🔯",  # six pointed star with middle dot
    "1f3bf": "🎿",  # ski and ski boot
    "1f480": "💀",  # skull
    "1f4a4": "💤",  # sleeping symbol
    "1f62a": "😪",  # sleepy face
    "1f355": "🍕",  # slice of pizza
    "1f3b0": "🎰",  # slot machine
    "1f539": "🔹",  # small blue diamond
    "1f538": "🔸",  # small orange diamond
    "1f63b": "😻",  # smiling cat face with heart-shaped eyes
    "1f63a": "😺",  # smiling cat face with open mouth
    "1f60d": "😍",  # smiling face with heart-shaped eyes
    "1f603": "😃",  # smiling face with open mouth
    "1f605": "😅",  # smiling face with open mouth and cold sweat
    "1f604": "😄",  # smiling face with open mouth and smiling eyes
    "1f606": "😆",  # smiling face with open mouth and tightly-closed eyes
    "1f60a": "😊",  # smiling face with smiling eyes
    "1f60f": "😏",  # smirking face
    "1f6ac": "🚬",  # smoking symbol
    "1f40c": "🐌",  # snail
    "1f40d": "🐍",  # snake
    "1f3c2": "🏂",  # snowboarder
    "2744": "❄",  # snowflake
    "26c4": "⛄",  # snowman without snow
    "26bd": "⚽",  # soccer ball
    "1f366": "🍦",  # soft ice cream
    "1f51c": "🔜",  # soon with rightwards arrow above
    "2198": "↘",  # south east arrow
    "2199": "↙",  # south west arrow
    "1f35d": "🍝",  # spaghetti
    "2747": "❇",  # sparkle
    "2728": "✨",  # sparkles
    "1f496": "💖",  # sparkling heart
    "1f64a": "🙊",  # speak-no-evil monkey
}

if __name__ == "__main__":
    print(parse_emoji_in_span('"Content": "<span classss="emoji emoji1f3c1"></span>",'))

    # for k,v in EmojiCodeMap.items():
    #     vv = EmojiCodeMap2.get(k,'')
    #     if vv == '':
    #         print(k, ' not exist')
    #     elif v != vv:
    #         print(k, v, vv, ' not match')

