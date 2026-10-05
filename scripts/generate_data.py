"""Generate sample travel PDF and CSV files into data/raw/"""
import csv, os, sys

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
os.makedirs(OUT, exist_ok=True)

# ── hotels.csv ────────────────────────────────────────────────────────────────
hotels = [
    ["hotel_id","name","city","country","stars","price_per_night_usd","amenities","review_score"],
    [1,"The Imperial Palace","Tokyo","Japan",5,420,"Pool,Spa,Gym,Restaurant,Airport Shuttle",9.2],
    [2,"Shinjuku Granbell Hotel","Tokyo","Japan",4,180,"Gym,Restaurant,Rooftop Lounge",8.7],
    [3,"Asakusa View Hotel","Tokyo","Japan",3,95,"Restaurant,Bar,City Views",8.1],
    [4,"Hotel Granvia Kyoto","Kyoto","Japan",4,210,"Spa,Gym,Restaurant,Tea Ceremony",8.9],
    [5,"Gion Hatanaka Ryokan","Kyoto","Japan",5,380,"Traditional Breakfast,Garden,Onsen",9.6],
    [6,"InterContinental Paris Le Grand","Paris","France",5,680,"Spa,Pool,Gym,Restaurant",9.1],
    [7,"Hotel du Louvre","Paris","France",4,340,"Restaurant,Bar,Louvre Views",8.8],
    [8,"Generator Paris","Paris","France",2,60,"Bar,Shared Kitchen,Social Spaces",8.3],
    [9,"Four Seasons Bali at Sayan","Ubud","Indonesia",5,750,"Infinity Pool,Spa,Yoga,Restaurant",9.5],
    [10,"Alaya Resort Ubud","Ubud","Indonesia",4,220,"Pool,Spa,Restaurant,Rice Field Views",9.0],
    [11,"Burj Al Arab","Dubai","UAE",7,2500,"Private Beach,Pools,Spa,Butler Service",9.7],
    [12,"Atlantis The Palm","Dubai","UAE",5,480,"Waterpark,Beach,Pools,Spa,Aquarium",9.1],
    [13,"Rove Downtown Dubai","Dubai","UAE",3,110,"Pool,Gym,Restaurant,Dubai Frame Views",8.6],
    [14,"Marriott Barcelona","Barcelona","Spain",5,390,"Pool,Spa,Gym,Restaurant",9.0],
    [15,"Hotel Arts Barcelona","Barcelona","Spain",5,520,"Beach,Pool,Spa,Michelin Restaurant",9.4],
    [16,"The Oberoi New Delhi","New Delhi","India",5,310,"Pool,Spa,Gym,Restaurant",9.2],
    [17,"Taj Mahal Palace Mumbai","Mumbai","India",5,420,"Pool,Spa,Multiple Restaurants",9.5],
    [18,"Capella Singapore","Singapore","Singapore",5,680,"Pool,Spa,Gym,Multiple Restaurants",9.6],
    [19,"Marina Bay Sands","Singapore","Singapore",5,580,"Infinity Pool,Casino,Spa,Restaurants",9.3],
    [20,"Zostel Delhi","New Delhi","India",1,15,"Shared Kitchen,Common Area,Lockers",8.0],
]
with open(os.path.join(OUT, "hotels.csv"), "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(hotels)
print("Created hotels.csv")

# ── flight_routes.csv ─────────────────────────────────────────────────────────
flights = [
    ["route_id","origin_city","origin_code","destination_city","destination_code","airline","duration_hours","avg_price_usd","class"],
    [1,"New York","JFK","London","LHR","British Airways",7.0,620,"Economy"],
    [2,"New York","JFK","Paris","CDG","Air France",7.5,580,"Economy"],
    [3,"New York","JFK","Tokyo","NRT","Japan Airlines",14.0,890,"Economy"],
    [4,"Los Angeles","LAX","Tokyo","NRT","Japan Airlines",11.5,760,"Economy"],
    [5,"Los Angeles","LAX","Bali","DPS","Garuda Indonesia",17.0,680,"Economy"],
    [6,"London","LHR","Dubai","DXB","Emirates",7.0,480,"Economy"],
    [7,"London","LHR","Singapore","SIN","Singapore Airlines",13.5,620,"Economy"],
    [8,"London","LHR","Bali","DPS","KLM",16.0,750,"Economy"],
    [9,"Sydney","SYD","Bali","DPS","Jetstar",6.0,280,"Economy"],
    [10,"Sydney","SYD","Tokyo","NRT","Qantas",9.5,820,"Economy"],
    [11,"Dubai","DXB","Bangkok","BKK","Emirates",6.0,380,"Economy"],
    [12,"Singapore","SIN","Tokyo","NRT","Singapore Airlines",7.0,340,"Economy"],
    [13,"Mumbai","BOM","Dubai","DXB","Air India",3.5,210,"Economy"],
    [14,"New York","JFK","London","LHR","British Airways",7.0,2800,"Business"],
    [15,"London","LHR","Dubai","DXB","Emirates",7.0,3200,"Business"],
    [16,"Los Angeles","LAX","Tokyo","NRT","ANA",11.5,4100,"Business"],
    [17,"New York","JFK","Paris","CDG","Air France",7.5,3600,"Business"],
    [18,"Sydney","SYD","London","LHR","Qantas",22.0,7800,"Business"],
    [19,"Delhi","DEL","Singapore","SIN","IndiGo",5.5,290,"Economy"],
    [20,"Bangkok","BKK","Bali","DPS","AirAsia",4.0,180,"Economy"],
]
with open(os.path.join(OUT, "flight_routes.csv"), "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(flights)
print("Created flight_routes.csv")

# ── package_deals.csv ─────────────────────────────────────────────────────────
packages = [
    ["package_id","name","destination","duration_days","price_per_person_usd","includes","best_season","highlights"],
    [1,"Japan Cherry Blossom Tour","Japan",10,3200,"Flights,Hotels,JR Pass,Tours","March-April","Shinkansen,Temples,Cherry Blossoms,Mt Fuji"],
    [2,"Bali Wellness Retreat","Bali",7,1800,"Flights,Resort,Yoga,Spa,Meals","April-October","Rice Terraces,Temples,Surfing,Cooking Class"],
    [3,"Paris Romance Package","France",5,2400,"Flights,4-Star Hotel,Seine Cruise,Museum Pass","April-June","Eiffel Tower,Louvre,Versailles,Fine Dining"],
    [4,"Dubai Luxury Escape","UAE",6,3800,"Flights,5-Star Hotel,Desert Safari,Burj Khalifa","October-April","Desert,Gold Souk,Waterpark,Skydiving"],
    [5,"Himalayan Trek Nepal","Nepal",14,2100,"Flights,Tea House Stays,Guide,Porter,Permits","March-May","Everest Base Camp,Sherpa Culture,Namche Bazaar"],
    [6,"Machu Picchu Discovery","Peru",9,2600,"Flights,Hotels,Train,Guide","May-September","Machu Picchu,Cusco,Sacred Valley,Inca Trail"],
    [7,"African Safari Kenya","Kenya",10,4500,"Flights,Safari Lodge,Game Drives,Park Fees,Meals","July-October","Big Five,Masai Mara,Hot Air Balloon"],
    [8,"Greek Island Hopper","Greece",10,2800,"Flights,Ferry Passes,Hotels","June-August","Santorini,Mykonos,Athens,Fresh Seafood"],
    [9,"Northern Lights Iceland","Iceland",6,2200,"Flights,Hotel,Northern Lights Tour,Blue Lagoon","November-February","Aurora Borealis,Geysers,Waterfalls"],
    [10,"Maldives Overwater Escape","Maldives",7,4200,"Flights,Overwater Bungalow,Meals,Snorkelling","November-April","Coral Reefs,Dolphin Watching,Sunset Cruise"],
    [11,"Vietnam Street Food Tour","Vietnam",10,1400,"Flights,Hotels,Food Tours,Ha Long Bay Cruise","February-April","Hanoi,Ho Chi Minh City,Hoi An,Pho"],
    [12,"Singapore City Break","Singapore",4,1600,"Flights,5-Star Hotel,City Tour,Gardens by the Bay","Year-round","Marina Bay,Sentosa,Hawker Food,Shopping"],
]
with open(os.path.join(OUT, "package_deals.csv"), "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(packages)
print("Created package_deals.csv")

# ── destination_guide.pdf ─────────────────────────────────────────────────────
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib.enums import TA_CENTER

    pdf_path = os.path.join(OUT, "destination_guide.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    BLUE  = colors.HexColor("#1a5276")
    LBLUE = colors.HexColor("#2e86c1")
    GREEN = colors.HexColor("#1e8449")

    title_s = ParagraphStyle("T", parent=styles["Title"],  fontSize=22, textColor=BLUE, alignment=TA_CENTER, spaceAfter=4)
    sub_s   = ParagraphStyle("S", parent=styles["Normal"], fontSize=11, textColor=colors.grey, alignment=TA_CENTER, spaceAfter=10)
    h1_s    = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=15, textColor=BLUE, spaceBefore=12, spaceAfter=4)
    h2_s    = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=11, textColor=LBLUE, spaceBefore=8, spaceAfter=3)
    body_s  = ParagraphStyle("B",  parent=styles["Normal"], fontSize=10, leading=14, spaceAfter=5)
    tip_s   = ParagraphStyle("Tp", parent=styles["Normal"], fontSize=9,  leading=13, leftIndent=10, textColor=GREEN, spaceAfter=3)

    story = []
    story.append(Paragraph("World Travel Destination Guide", title_s))
    story.append(Paragraph("Your Complete Reference for Top Global Destinations", sub_s))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "This guide covers the world's most sought-after travel destinations with essential information "
        "on top attractions, local cuisine, transport, visa requirements, budgeting, and practical tips "
        "for a smooth and memorable journey.", body_s))

    destinations = [
        ("JAPAN", "Tokyo & Kyoto", [
            ("Overview", "Japan blends ancient traditions with cutting-edge modernity. From Tokyo's neon-lit streets and world-class ramen to Kyoto's serene temples and geisha culture, it offers a travel experience unlike anywhere else. The country is renowned for exceptional food, punctual transport, and genuine hospitality."),
            ("Must-See Attractions", "Senso-ji Temple (Asakusa) — Tokyo's oldest temple, best visited at dawn. Shibuya Crossing — the world's busiest pedestrian intersection. Fushimi Inari Shrine — 10,000 vermillion torii gates winding up a forested mountain. Arashiyama Bamboo Grove — ethereal bamboo forest west of Kyoto. Kinkaku-ji (Golden Pavilion) — gold-leaf covered Zen temple reflected in a mirror pond."),
            ("Food & Drink", "Japan has more Michelin stars than any other country. Must-try: Ramen, Sushi and Sashimi, Tempura, Yakitori, Okonomiyaki, and Matcha desserts. Convenience stores (konbini like 7-Eleven) sell surprisingly excellent food 24/7. Sake, Japanese whisky, and craft beer are popular drinks."),
            ("Practical Tips", "Get a JR Pass before leaving your home country. Buy an IC card (Suica/Pasmo) for local trains. Cash is essential — many places are cash-only. Bow slightly when greeting. Remove shoes when entering homes and traditional restaurants. Avoid eating or drinking while walking."),
            ("Budget", "Budget: $50-70/day. Mid-range: $130-200/day. Luxury: $400+/day. Best season: March-May (cherry blossoms) and September-November (autumn foliage)."),
        ]),
        ("FRANCE", "Paris & Beyond", [
            ("Overview", "France is the world's most visited country. Paris dazzles with iconic monuments, world-class museums, and legendary cuisine. Beyond the capital: the French Riviera, wine regions of Bordeaux and Burgundy, Loire Valley chateaux, and lavender fields of Provence all await."),
            ("Must-See Attractions", "Eiffel Tower — most visited paid monument in the world; stunning at night when lit up. Louvre Museum — home to the Mona Lisa and 35,000 other masterpieces. Palace of Versailles — opulent royal palace with spectacular gardens (45 min from Paris by RER C). Sacre-Coeur Basilica — crowning Montmartre hill with panoramic city views. Musee d'Orsay — world's finest collection of Impressionist art."),
            ("Food & Drink", "French cuisine is UNESCO-listed as Intangible Cultural Heritage. Daily essentials: fresh croissant and cafe au lait from a neighbourhood boulangerie. Classic dishes: French Onion Soup, Coq au Vin, Steak Frites, Croque Monsieur, Crepes Suzette, Creme Brulee. Wine regions: Bordeaux (reds), Burgundy (Pinot Noir/Chardonnay), Champagne, Loire (whites)."),
            ("Practical Tips", "Always greet shopkeepers with Bonjour — it is considered rude not to. Tipping is not mandatory but 5-10% is appreciated. Paris Museum Pass saves money and skips queues. Many museums are free on the first Sunday of the month. Metro covers all major sights — validate your ticket before boarding."),
            ("Budget", "Budget: $80-100/day. Mid-range: $180-250/day. Luxury: $500+/day. Best season: April-June and September-October."),
        ]),
        ("INDONESIA", "Bali — Island of the Gods", [
            ("Overview", "Bali offers extraordinary natural beauty, rich Hindu culture, world-class surfing, yoga retreats, and exceptional value for money. From Ubud's cultural heart to Seminyak's beach clubs and Uluwatu's dramatic clifftop temple, every part of the island delivers magic."),
            ("Must-See Attractions", "Tegallalang Rice Terraces — stunning UNESCO-listed terraced paddies north of Ubud. Mount Batur — active volcano with a legendary 2-hour sunrise trek. Tanah Lot Temple — ancient Hindu temple perched on a sea rock at sunset. Ubud Monkey Forest — 700 long-tailed macaques among ancient temple ruins. Nusa Penida Island — Kelingking Beach's T-Rex cliff and Crystal Bay snorkelling."),
            ("Food & Drink", "Balinese food is aromatic and rich. Must-try: Nasi Goreng (national fried rice dish), Babi Guling (ceremonial suckling pig — best in Ubud), Satay with peanut sauce, Gado-Gado (vegetable salad with peanut sauce), Mie Goreng (fried noodles). Drink fresh young coconut water straight from the nut."),
            ("Practical Tips", "Hire a private driver for $35-50/day — essential for flexibility. Respect temple etiquette: wear a sarong and sash, remove shoes. Bargain in markets — start at 30-40% of asking price. Use the Grab app for affordable rides in towns. Avoid tap water entirely. The wet season (November-March) brings heavy afternoon rains."),
            ("Budget", "Budget: $25-40/day. Mid-range: $70-120/day. Luxury: $250-750/day. Best season: April-October (dry season)."),
        ]),
        ("UAE", "Dubai — City of the Future", [
            ("Overview", "Dubai is a city of superlatives — world's tallest building, largest mall, and most luxurious hotels. Built from desert sands in decades, it combines futuristic architecture, world-class shopping and dining, desert adventures, and a rich Arabian cultural heritage."),
            ("Must-See Attractions", "Burj Khalifa — world's tallest building at 828m; observation deck on floor 124 offers views across the Gulf. Dubai Mall — 1,200 shops, an indoor ice rink, and an aquarium under the same roof. Palm Jumeirah — artificial palm-shaped island visible from space. Dubai Desert Safari — dune bashing, camel riding, and traditional Bedouin camp dinner. Gold Souk and Spice Souk — traditional covered markets in historic Deira district."),
            ("Food & Drink", "Dubai is a global food capital with cuisine from 200+ nationalities. Must-try local dishes: Shawarma (spit-roasted meat wrap), Hummus, Al Harees (wheat and meat porridge), Luqaimat (sweet dumplings with date syrup), Camel milk products. Note: alcohol is available in licensed hotels and restaurants but is not sold in supermarkets."),
            ("Practical Tips", "Dress modestly in public areas and souks — shoulders and knees covered. Alcohol only in licensed venues. Ramadan months bring restricted daytime eating/drinking in public. Dubai Metro is efficient, air-conditioned, and affordable. Taxis and Careem (Uber equivalent) are widely available and metered."),
            ("Budget", "Budget: $80-120/day. Mid-range: $200-350/day. Luxury: $500-2000+/day. Best season: November-March (mild weather, outdoor activities possible)."),
        ]),
    ]

    for country, subtitle, sections in destinations:
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
        story.append(Spacer(1, 6))
        story.append(Paragraph(country, h1_s))
        story.append(Paragraph(subtitle, h2_s))
        for sec_title, sec_body in sections:
            story.append(Paragraph(sec_title, h2_s))
            story.append(Paragraph(sec_body, body_s))
        story.append(Spacer(1, 8))

    # Comparison table
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Quick Destination Comparison", h1_s))
    table_data = [
        ["Destination", "Best Season", "Budget/Day (USD)", "Visa", "Safety"],
        ["Tokyo, Japan",      "Mar-May, Sep-Nov", "$50 – $400+",  "eVisa / Free",        "Very Safe"],
        ["Kyoto, Japan",      "Mar-May, Oct-Nov", "$50 – $380+",  "eVisa / Free",        "Very Safe"],
        ["Paris, France",     "Apr-Jun, Sep-Oct", "$80 – $500+",  "Schengen",            "Generally Safe"],
        ["Bali, Indonesia",   "Apr-Oct",          "$25 – $750+",  "Visa on Arrival",     "Safe"],
        ["Dubai, UAE",        "Nov-Mar",          "$80 – $2000+", "Free (90+ nations)",  "Very Safe"],
        ["Barcelona, Spain",  "May-Jun, Sep-Oct", "$60 – $450+",  "Schengen",            "Generally Safe"],
        ["New York, USA",     "Apr-Jun, Sep-Nov", "$100 – $700+", "ESTA / Visa",         "Generally Safe"],
        ["Singapore",         "Year-round",       "$70 – $600+",  "Free (most nations)", "Very Safe"],
        ["Machu Picchu, Peru","May-Sep",          "$40 – $350+",  "Free (most nations)", "Safe in tourist zones"],
    ]
    tbl = Table(table_data, colWidths=[3.8*cm, 3.4*cm, 3.2*cm, 3.6*cm, 3.0*cm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0),  BLUE),
        ("TEXTCOLOR",     (0,0), (-1,0),  colors.white),
        ("FONTNAME",      (0,0), (-1,0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [colors.white, colors.HexColor("#eaf4fb")]),
        ("GRID",          (0,0), (-1,-1), 0.4, colors.HexColor("#aed6f1")),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("PADDING",       (0,0), (-1,-1), 5),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 14))

    story.append(Paragraph("Essential Travel Tips for Every Destination", h1_s))
    tips = [
        "Check visa requirements at least 8 weeks before travel — requirements change frequently.",
        "Get comprehensive travel insurance covering medical emergencies, cancellations, and lost luggage.",
        "Keep digital copies of your passport, visa, and insurance in both email and cloud storage.",
        "Notify your bank of travel dates to prevent your card being blocked abroad.",
        "Download offline maps (Google Maps offline or Maps.me) before you go.",
        "Use bank ATMs at your destination for the best currency exchange rates — avoid airport kiosks.",
        "Book popular attractions online in advance — Louvre, Sagrada Familia, and Machu Picchu sell out.",
        "Learn 5-10 words in the local language — even 'hello' and 'thank you' go a long way.",
        "Pack a universal power adapter and a portable power bank for long travel days.",
        "Research local customs around dress, food, and greetings before you arrive.",
    ]
    for tip in tips:
        story.append(Paragraph(f"• {tip}", tip_s))

    doc.build(story)
    print("Created destination_guide.pdf")

except ImportError:
    print("reportlab not installed. Run: pip install reportlab")
    sys.exit(1)

print(f"\nAll files saved to: {os.path.abspath(OUT)}")
print("Files:", os.listdir(OUT))
