import pandas as pd
import numpy as np

beer_list = [
    'Kronenbourg 1664 Blanc',
    'Kabrew Gyeongbokgung Royal Pride IPA',
    'ARK Seoulite Ale',
    'Kabrew Kumiho India Pale Ale',
    'Kabrew Kumiho Peach Ale',
    'Goose Island Goose IPA',
    'Goose Island Duck Duck Goose',
    'Goose Island Matilda',
    'Goose Island Bourbon County Stout',
    'Goose Island Sofie',
    'Goose Island Summertime',
    "Goose Island Pepe Nero",
    "Goose Island Honkers Ale",
    "Goose Island 312 Urban Wheat Ale",
    "Guinness Draught",
    "Guinness Extra Stout (North America)",
    "Guinness Foreign Extra Stout",
    "Guinness Black Lager",
    "Kirin Lager",
    "Kirin Ichiban",
    "Kabrew Namsan Mountain Premium Citra Ale",
    "Budweiser",
    "Budweiser Select",
    "Budweiser Budvar",
    "Budweiser Budvar Dark",
    "Cyprus Venus",
    "Desperados",
    "Desperados Red",
    "Hite D (Dry Finish)",
    "Lagunitas India Pale Ale (IPA)",
    "Lagunitas DayTime",
    "Lagunitas Maximus IPA",
    "Tsingtao Laoshan 4.0% 10°P",
    "Tsingtao Laoshan 4.7% 11°P",
    "Leffe Brune",
    "Mango Lingo",
    "Hite Prime Max",
    "Magners Juicy Apple",
    "Miller Genuine Draft (MGD)",
    "Miller Lite",
    "Miller Chill Chelada Style",
    "Miller High Life",
    "San Miguel Pale Pilsen",
    "Sapporo Draft Beer",
    "Sapporo Reserve",
    "Sapporo premium lager",
    "Suntory The Premium Malt's",
    "Suntory The Premium Malt's Kaoru Ale",
    "Spaten Münchner München",
    "Spaten Oktoberfest Ur-Märzen",
    "Spaten Optimator",
    "Stella Artois",
    "Singha Draft",
    "Somersby Apple Cider",
    "Warsteiner Premium Verum",
    "Warsteiner Premium Dunkel",
    "Beck's",
    "Beck's Dark",
    "BrewDog Punk AF",
    "BrewDog Punk IPA (5.6%)",
    "Blue Moon Belgian White",
    "Asahi Super Dry",
    "Asahi Super Dry Black",
    "Asahi Clear Prime Rich",
    "Apple Fox",
    "에델바이스 스노우프레쉬" : "Edelweiss Weissbier Snowfresh",
    "에딩거 바이스비어" : "Erdinger Weissbier",
    "예비스" : "Sapporo Yebisu",
    "이슬 톡톡" : "Isul Tok Tok",
    "이슬 톡톡 파인애플" : "Isul Tok Tok Pineapple",
    "스타우트" : "Hite Black Beer Stout",
    "Egger Naturtrüber Zitronenradler",
    "Egger Grapefruit Radler",
    "Jeju Baengnokdam Ale",
    "Jeju Seongsan Ilchulbong Ale",
    "Jeju Wit Ale",
    "Jeju Pellong Ale",
    "Cass Light",
    "Cass Fresh",
    "Carlsberg Pilsner",
    "Corona Extra",
    "Corona Light",
    "Kozel Černý (Dark) 10°",
    "Kozel Premium Lager 12°",
    "Queen's Ale Blonde Type",
    "Queen's Ale Extra Bitter Type",
    "Kloud Original Gravity",
    "Tiger Beer",
    "Tiger Radler Lemon",
    "Terra",
    "Tsingtao",
    "Tsingtao Wheat Beer",
    "Tsingtao Draft Beer 11º (Pure Draft Beer)",
    "Paulaner Original Münchner Hell (Premium Lager)",
    "Paulaner Oktoberfest Bier (Wiesn Bier)",
    "Paulaner Salvator",
    "Paulaner Hefe-Weissbier",
    "Patagonia",
    "Patagonia Amber Lager",
    "Patagonia Weisse",
    "Patagonia Bohemian Pilsener",
    "Peroni",
    "Happoshu Filgood",
    "FiLite",
    "Filite Fresh Cool & Clear",
    "Filite Weizen",
    "Pilsner Urquell",
    "Fitz Super Clear",
    "Harbin Beer",
    "Heineken",
    "Heineken 0.0",
    "Heineken Dark Lager",
    "Hite Beer",
    "Hite Extra Cold",
    "Hite Zero",
    "Hoegaarden",
    "Hoegaarden Rosée",
    "Hop House 13 Lager",
    "Kabrew Hoptandu IPA",
]

# 데이터프레임으로 저장
beer_list = pd.DataFrame(data=beer_list, columns=['검색이름'])