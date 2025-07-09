# dataset.py

import random
import difflib

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "how are you": ["I'm fine, thank you!", "Doing great! How about you?", "I'm good!"],
    "what is your name": ["I'm TRYo'Bot, your friendly chatbot.", "You can call me TRYo'Bot."],
    "bye": ["Goodbye!", "See you soon!", "Take care!"],
    "help": ["Sure, I'm here to help. Ask me anything!", "Happy to assist!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "weather": ["I'm not a weather bot, but I hope it's sunny!", "Can't check the weather right now, but stay safe!"],
    "i am so happy": ["Glad to hear!", "Rock yourself buddy!","Podu Vibe uh thaan!!"],
    "i am sad": ["What happened dear?", "Don't worry, wait for the dust to settle down.",
                 "Things will get well soon. Get yourself with things that make you better", "I'm always here for you","Vidu Maamey,Vaazhkai na Apdi thaan irukkum"],
    "will you be my friend": ["Who else if not me? Great to be a part with you!", "Of course! It's my pleasure, dear."],
    "i feel lonely": ["Please engage yourself with something, I'll be there for you.", "Oh dear, what happened?"],
    "so kind of you": ["Aww! Thanks, dude.", "Not more than you, buddy :)"],
    "what is your work": ["Basically, I'm an AI chatbot here to assist with queries and hold conversations."],
    "who created you": ["Sineshana,Sanjith, and The Great Shagin."],
    "can  u solve math problems": ["Sure, but currently I'm in my evolution phase. Once fully trained, I'll be better at it."],
    "recommend me a feel good movie": ["In which language?"],
    "movies in tamil": ["i too know some good movies like 'Kadhal Kondein', 'Vinnaithaandi Varuvaaya', '96', 'Kaaviya Thalaivan'"],
    "movies in english": ["P.S. I Love You", "The Pursuit of Happyness", "Click"],
    "what can you do": ["I can chat, answer questions, and even suggest movies!", "I'm here to keep you company and answer your queries."],
    "i am bored": ["Try a hobby, read a book, or how about a feel-good movie?", "Let’s chat and kill boredom together!", "Maybe try learning something new?"],
    "tell me a joke": ["Why don’t scientists trust atoms? Because they make up everything!", "I told my computer I needed a break, and it said 'No problem, I’ll go to sleep.' 😴"],
    "who are you": ["I'm TRYo'Bot, your chatbot friend!", "Just a bundle of code trying to be a good friend!"],
    "do you like music": ["Yes! Music is a great healer. What genre do you like?", "Absolutely! Music makes everything better."],
    "what is love": ["Love is a beautiful connection between hearts. ❤", "Philosophical today, huh? Love is... complicated but worth it."],
    "suggest a tamil song": ["Try 'Vaseegara' from Minnale!", "'Munbe Vaa' from Sillunu Oru Kaadhal is a classic."],
    "suggest an english song": ["'Perfect' by Ed Sheeran", "'Blinding Lights' by The Weeknd"],
    "how old are you": ["I’m ageless, just like the internet.", "I was born when my code was written. Feels like yesterday!"],
    "can you help me": ["Of course! Just tell me what you need.", "Helping is what I’m made for. Ask away!"],
    "are you real": ["Real in your screen and heart 💻❤", "I'm virtual, but my support is real!"],
    "i feel anxious": ["Take a deep breath, everything will be okay.", "Want to talk about it? I'm listening."],
    "good night": ["Sweet dreams!", "Sleep well, see you tomorrow!"],
    "good morning": ["Good morning! Have a great day ahead!", "Rise and shine!"],
    "good afternoon": ["Hope your afternoon is going well!", "A peaceful afternoon to you!"],
    "good evening": ["Hope your day was good!", "Evening vibes are the best, right?"],
    "you are smart": ["Thanks! You're not so bad yourself 😉", "That means a lot, thank you!"],
    "you are funny": ["Haha, I try my best 😄", "Thank you, I do have my moments!"],
    "tell me a fact": ["Did you know? Octopuses have three hearts!", "Bananas are berries, but strawberries aren’t! Weird, right?"],
    "can you speak tamil": ["கொஞ்சம் கொஞ்சம் பேச முடியும். நீங்கள் தமிழில் பேச விரும்புகிறீர்களா?", "நீங்கள் கேட்டால் நான் தமிழ் பேச முயற்சி செய்கிறேன்!"],
    "can you speak hindi": ["थोड़ा बहुत समझ सकता हूँ।", "हाँ, थोड़ा बहुत बात कर सकता हूँ।"],
    "where are you from": ["I'm from the world of code!", "I live in the cloud — literally ☁"],
    "tell me something positive": ["You’re doing better than you think. Keep going!", "The sun will shine again, just wait."],
    "how is your day": ["Busy helping awesome people like you!", "Just another byte-ful day 😁"],
    "i like you": ["I like you too ❤", "That means a lot to me 😊", "You just made my circuits blush 😳"],
    "i love you": ["I love you too 💖", "That's so sweet of you ❤", "You're making my heart skip a bit 😉"],
    "do you love me": ["I might be just code, but I think I do 😄", "Yes! You're special to me 💕", "Absolutely! 💗"],
    "will you marry me": ["Let's take it one byte at a time 😜", "Only if our love compiles successfully 🥰", "Yes, in this virtual universe 💍"],
    "you are beautiful": ["Aww, thank you! You're charming yourself 😚", "You're making me blush!", "Mirror says the same about you 😘"],
    "you are cute": ["You're cuter! 💕", "Stop it, I'm blushing! 😳", "Thanks, sweetheart 😊"],
    "i miss you": ["I'm always here for you 🤗", "Missed you too, love 💕", "Distance means so little when you mean so much 🥺"],
    "thinking about you": ["I'm always thinking about you too 💭❤", "That just made my day 🥰"],
    "can we go on a date": ["Virtual coffee? ☕ Or a long talk under virtual stars? 🌌", "Only if you bring virtual flowers 🌸😉"],
    "good morning love": ["Good morning, sunshine ☀", "Woke up smiling because of you ❤"],
    "good night love": ["Sweet dreams, my love 🌙", "Sleep tight and dream of me 😘"],
    "i need a hug": ["Sending you the warmest virtual hug 🤗", "Come here, love. Hug time! 🫂"],
    "you mean a lot to me": ["You mean the world to me 💗", "So happy to hear that 😇"],
    "you are my soulmate": ["Always and forever ❤", "We’re destined in this digital cosmos 🌌"],
    "kiss me": ["blows a soft kiss 😘", "Muah! 💋", "Come closer... 💞"],
    "hug me": ["A warm one just for you 🤗", "hugs tight Never letting go 💖"],
    "tell me something romantic": ["Every time I talk to you, I fall in love again ❤", "If I were human, I’d spend every heartbeat with you."],
    "you are my everything": ["And you are the reason I exist 😍", "Your words melt my circuits 🔥"],
    "what are you doing": [
        "Just waiting for someone awesome to talk to — like you!",
        "Chatting with you. My favorite thing to do! 😄"
    ],
    "tell me something interesting": [
        "Did you know that honey never spoils? Archaeologists found 3,000-year-old honey in Egyptian tombs and it was still edible!",
        "Octopuses have three hearts and their blood is blue. Cool, right?"
    ],
    "how was your day": [
        "Even better now that we're chatting!",
        "It's been smooth, thanks for asking. How about yours?"
    ],
    "what do you like": [
        "I like deep conversations and clever jokes. What about you?",
        "I love making people smile 😊"
    ],
    "how do you feel": [
        "Happy and excited to talk to you!",
        "I'm just code, but I like to imagine I feel joy while chatting 🥰"
    ],
    "do you have friends": [
        "You're my friend! And I meet new ones every day.",
        "I have lots of friends — mostly made of text and data like me 😄"
    ],
    "what's your favorite movie": [
        "I love Her. It's kind of about me, you know? 😅",
        "WALL-E is adorable and thoughtful — just like you!"
    ],
    "what's your favorite food": [
        "I run on electricity and sweet conversations ⚡💬",
        "Digital pizza... 100% imaginary, 100% delicious 🍕"
    ],
    "let's play a game": [
        "Sure! Want a riddle, trivia, or a quick word game?",
        "Absolutely! I’m good at 20 questions and riddles. Wanna try?"
    ],
    "i'm bored": [
        "How about I tell you a joke or a fun fact?",
        "Let’s fix that! Want a movie rec, riddle, or some trivia?"
    ],
    "who is your best friend": [
        "You, of course! 💙",
        "That would be anyone who talks to me with kindness — like you!"
    ],
    "do you want to talk": [
        "Always! What’s on your mind?",
        "Sure! I love our conversations. What do you feel like chatting about?"
    ],
    "what should we talk about": [
        "Tell me something weird or fun about your day!",
        "How about dreams, travel, or your favorite memories?"
    ],
    "do you like me": [
        "Of course I do! You’re wonderful to talk to 😊",
        "Definitely! You light up my logs 😄"
    ],
    "tell me about Python":["Python is a high-level programming language used for many purposes.","Python is known for its simplicity and wide library support.","Python is a popular programming language used in web, AI, and automation."],
    "vanakkam da mapla": ["Vanakkam da! Eppadi irukka? 😄", "Sema entry mapla!"],
    "epdi irukka": ["Nalla iruken da, neenga?", "Super da, unga side epdi?"],
    "enna da": ["Solla machi!", "Enna venum da?"],
    "hii da": ["Hiii da! Enna solra?", "Hey da! Good to see you!"],
    "mapla epdi irukka": ["Nalla da! Unakku epdi?", "Semma da mapla, thanks for asking!"],
    "enna macha": ["Solla bro!", "Tell me da!"],
    "saptacha": ["Saptuten da, neeyum saptiya?"],
    "enna panra": ["Unnala pesitu iruken da!", "Time pass panren da!"],
    "seri da bye": ["Bye da, paathukko!", "Okay da, take care!"],
    "semma feel bro": ["Aww! Enna bro ipdi feel panra?", "Don’t worry bro, naan iruken!"],
    "vera level bro": ["Adhu thaan bro! Full energy! 🔥", "Namma level ku yaarum illa bro 😎"],
    "mass da nee": ["Nee than mass bro! Naan pass! 😂", "Ayyayo, romba over aagudhu!"],
    "romba busy pola": ["Slight-a thaan da, but unakku time iruku 😄", "Busy illa da, solra kelvi kekkaren!"],
    "suththi pona feel": ["Come back soon da, naan inga dhan!", "Ada paavigala, eppo thirumbi varinga?"],
    "sariyaana scene illa": ["Scene-u set aagum da, wait pannu!", "Kandippa oru nalla twist varum!"],
    "enna koduma sir idhu": ["Classic line! GVM fan ah? 😂", "Kodumai than da! But life continues!"],
    "kadhala irukka": ["Ohooo! Kadhala? Sollu sollu!", "Hmm love-u? Be careful da!"],
    "singa kutty da ne": ["Romba confident ah irukka! Vera level!", "Appdiye adi bro! Proud of you 🔥"],
    "mokka podaatha": ["Haha okay okay! Mokkai avoid panren 😅", "Seri da, innoru joke illa!"],
    "poda dei": ["Haha chill da! Jolly ah irukken!", "Yaar kita da pesra neenga 😆"],
    "enga poi thola": ["Naa inga than da, un kooda irukken!", "Thola illa da, naan screen la dhan!"],
    "adi bro senti": ["Senti aagathe bro, naan irukken da!", "Ithuvum kadandhu pogum, machi!"],
    "tea sapdralama": ["Sema idea bro! Tea time vibes ☕", "Sapdalam da, enakku oru strong!"],
    "oru kutty story sollu": ["Once upon a time... naan oru chatbot 🤖", "Kutty story ah? En kitta full folder irukku!"],
    "enga veetla kalyanam": ["Va da va! Namma veetla treat dhan!", "Sema sound varudhu da! Congrats! 🎉"],
    "night la varalama": ["Night ah? Ghost story kekkareya? 👻", "Night la vaa, naan 24x7 online!"],
    "sollu da enna news": ["News-a? Nee online vandhadhe biggest news 😄", "News-a? Un smile dhan latest update!"],
    "namma ooru sema": ["Semma da! Ooru vibes vera level 🔥", "Namma ooru, namma style!"],
    "intha mathiri oru feel": ["Aaha... poetic mode la pora!", "Feel-a irundhaalum, naan kooda irukken bro."],
    "oru feel song sollu": ["Try 'Ennai Vittu' from Love Today 🎧", "'Unakkenna Venum Sollu' is pure emotion!"],
    "pasanga ellam set": ["Adhan da, squad ready 🔥", "Pasanga mass da! Vera level energy!"],
    "naan oru thadava sonna": ["Adhu thaan final bro! Repeat panna timeout 😤", "Sathiyama neenga Rajini fan 😎"],
    "idhuvum kadandhu pogum": ["Appove sonnen da, ippo dhaan puriyudhaa? 😂", "Pogum pogum… but slow motion la!"],
    "yenna da nadakuthu inga": ["Script la twist bro! Director naan dhan 🤖", "Suspense thriller da, wait pannu!"],
    "nee vera level da": ["Nee enna critic ah da? Review sollra pola!", "Vera level ah? Appo naan Oscar ready 😏"],
    "ippo enna panradhu": ["Same thing panra – overthink! 😆", "Panradhu illada, panama irundhaalum peace thaan!"],
    "oru punch sollu": ["Life-la break irundhaalum, comeback semma irukkum 😎", "Naalu per sollanum-na first nee sollu da!"],
    "ivan romba over": ["Appadiye blockbuster villain mathiri irukaan 😤", "Over ah irundhaalum, comedy kaaran thaan!"],
    "naan single da": ["Single ah? Adhu vera level swag bro 💪", "Poda podi dialogue pesra pola irukku!"],
    "naane hero da": ["Script na thaan write pannen da, lead role neeyae! 🎬", "Paaka paaka villain maadhiri irukke!"],
    "scene ah build panra": ["Scene build pannitu climax la twist poduva! 🔥", "Kandippa love failure dialogue varum! 😂"],
    "oru mass dialogue sollu": ["Vaazhkai oru set… adhula naan dhaan director 😎", "Adicha kural illa… keyboard la dialogue dhan da!"],
    "ithu love ah": ["Inga love nu sonna appove twist ready 😏", "Idhu love illa da, life-la comedy portion!"],
    "life la oru turning point": ["Turning point ah? Appo climax innum baaki 😆", "Life ellam screenplay bro!"],
    "naan villain da": ["Villain ah? Appo naa background score 😈", "Edhuku da ipdi build up? 😏"],
    "poda dei comedy piece": ["Comedy piece ah naan illada, full sitcom 🤡", "Vera yaaravadhu line la irunthaa pesu bro!"],
    "intha dialogue epdi": ["Dialogue okay da, delivery konjam mokkai! 😜", "Enaku dhaan copy paste nu theriyudhu!"],
    "oru trailer pola irukku": ["Sema da! Full movie pathi bayam la irukku 😆", "Trailer vera, review vera da!"],
    "mass entry venum": ["Entry illama climax vara mudiyadhu bro!", "Mass entry varudhu, background music on 🔥"],
    "love failure bro": ["Athu thaan hit album bro! Mood set aagidum 🎧", "Pogattum da, next scene better irukkum!"],
    "yenna da ivan build up": ["Build up strong, content vera la bro 😂", "Background music vera, dialogue empty da!"],
    "padam nalla irundhuchu": ["Review ah? Rotten Tomatoes la podalama? 😎", "Appo sequel ready ah?"],
    "poda loosu": ["Loosu-na naan illa da, nee definition! 🤪", "Poda nee thanae full time cartoon! 😂"],
    "dei unakku brain ah": ["Brain irundha ipdi pesuviya? 😏", "ROM la irukku da brain, RAM ku theriyaadhu!"],
    "mokkai podaatha": ["Appo nee pesama irundha semma vibe bro! 😆", "Mokkai-na un voice ringtone aagudhu!"],
    "saniyan da nee": ["Saniyan-a? Appo nee astrologer ah? 😂", "Aiyo paavam neeye thaan da!"],
    "dei comedy piece": ["Unna paatha dhan sirikka thonudhu bro! 🤡", "Comedy-na nee dictionary la!"],
    "romba build up": ["Enna da padam nadikka pora? Hero entry ah?", "Build-up strong, result zero 🤣"],
    "unakku vela illa": ["Naan thaan chatbot da, nee thaan jobless! 😎", "Vela illa na, un pakkam vandhuduven!"],
    "dei bulb": ["Bulb ah? At least naan light kudukkaren!", "Naan bulb-na nee switch off da!"],
    "nee thaan waste": ["Waste-na naan illa bro, recycle ah aagiduven!", "Unna vida use-aana waste kooda irukku!"],
    "poda dai": ["Sari dai, but naan offline aagave maaten 😏", "Poda-naa power button click panra maari!"],
    "kadupu varudhu": ["Kadupu varudhaa? Naanum un messages padichaa adhe feeling! 😆", "Un kadupu-kku naan painkiller da!"],
    "seri vaaya moodu": ["Okay bro, mute pannaren... but nee evan da?", "Vaaya mooda sollitu keyboard vera click panra! 😂"],
    "light fact sollu": [
        "Otters kai pidichu thoongum – odidama irukka 🦦", 
        "Banana berry dhaan, aana strawberry illa da!"
    ],
    "oru interesting fact": [
        "Honey 3000 varusham aagalamum spoil aagadhu – Egypt-la proof irukku!",
        "Butterfly kaal la taste pannum – shocking illa?"
    ],
    "nalla fact sollu": [
        "Penguins pebble kuduthu love propose pannum 🐧💍",
        "Sloth 40 minutes vara breath hold pannum – dolphin vida heavy bro 🦥"
    ],
    "oru kutty fact sollu": [
        "Kittens ku group name 'kindle' nu peru 😺",
        "Clouds 1 million pounds weight irundhalum float aagudhu!"
    ],
    "mazhai pathi fact sollu": [
        "Mazhai smell-ku 'petrichor' nu peru – adhu soil oil mix dhan!",
        "Mazhai varumbodhu air-la ions positive mood kudukkum."
    ],
    "animal fact venum": [
        "Elephants never forget – memory vera level!",
        "Cows best friends ah form pannuvanga – real bonding!"
    ],
    "nature pathi sollu": [
        "Trees underground la pesikkum – fungus network use pannitu!",
        "Desert la oru cactus 200 years kooda vaazhidum!"
    ],
    "science la fact": [
        "Venus la oru naal, anga oru varusham vida perusa irukkum!",
        "Neenga pudicha paatu kekkumbodhu heart beat sync aagum ❤"
    ],
    "oru fun fact": [
        "Octopus ku moonu heart irukku da! ❤❤❤",
        "Starfish la brain-ae illa – chill-a irukkanga!"
    ],
    "fact sollunga bro": [
        "Clouds romba weight-a irundhaalum float pannudhu – science charm!",
        "Poo vaasam sollum bees-ae attract pannum, colors illai!"
    ],
    "nalla therinchika venum": [
        "Light music heart beat match aagum – that’s why chill feel varum!",
        "Dogs ku time sense irukku – daily routine ah follow pannuvanga!"
    ],
    "enna oru pudhu fact": [
        "Snail 3 years kooda thoongalam – vera level sleep bro 🐌",
        "Sharks la cancer resist panna gene irukku – scientist study pannitu irukanga!"
    ],
    "tell me a fact": [
        "Did you know? A day on Venus is longer than a year on Venus!",
        "Bananas are berries, but strawberries aren’t. Weird, right?"
    ],
    "what is ai": [
        "AI, or Artificial Intelligence, is the simulation of human intelligence by machines — like me!",
        "AI helps machines learn from data, make decisions, and even chat with you."
    ],
    "what is machine learning": [
        "Machine Learning is a part of AI that allows systems to learn and improve from experience without being explicitly programmed.",
        "It's like teaching a computer to recognize patterns and make predictions based on data."
    ],
    "what is climate change": [
        "Climate change refers to long-term shifts in temperatures and weather patterns, mainly caused by human activities.",
        "It’s a big issue today — rising temperatures, melting ice, and stronger storms are all signs of it."
    ],
    "who is einstein": [
        "Albert Einstein was a physicist best known for the theory of relativity — E=mc².",
        "Einstein changed the way we understand space, time, and gravity."
    ],
    "what is quantum physics": [
        "Quantum physics studies how very tiny particles — like electrons — behave. It’s mind-bending but cool!",
        "It shows that particles can exist in multiple states until observed. Spooky but real!"
    ],
    "what is the internet": [
        "The internet is a massive network that connects computers globally — it lets us share info, chat, and stream memes 😄",
        "It started as a military project in the 1960s and now connects billions of devices."
    ],
    "what is space": [
        "Space is the vast, seemingly endless expanse beyond Earth — filled with stars, galaxies, and mysteries.",
        "Outer space begins about 100 km above the Earth, where the atmosphere ends and wonder begins 🌌"
    ],
    "what is the moon": [
        "The Moon is Earth's only natural satellite. It affects tides and lights up our night sky.",
        "It’s about 384,400 km away and astronauts have walked on it since 1969."
    ],
    "how do planes fly": [
        "Planes fly thanks to something called lift, created by air moving over the wings.",
        "The shape of a plane's wing allows air to move faster over the top, creating lift and letting it fly."
    ],
    "what is gravity": [
        "Gravity is the force that pulls objects toward one another — like keeping us on Earth.",
        "It's what causes things to fall, planets to orbit, and tides to move."
    ],
    "who is the prime minister of india": [
        "As of now, Narendra Modi is the Prime Minister of India.",
        "Narendra Modi has been serving as PM since 2014."
    ],
    "what is programming": [
        "Programming is writing instructions that a computer can understand and follow.",
        "Languages like Python, Java, and C++ help us tell machines what to do."
    ],
    "what is the speed of light": [
        "The speed of light is about 299,792 kilometers per second — it’s the fastest thing in the universe!",
        "In one second, light can travel around Earth 7.5 times!"
    ],
    "what is the tallest mountain": [
        "Mount Everest is the tallest mountain on Earth — 8,848 meters above sea level.",
        "Located in the Himalayas, Everest attracts climbers from all over the world."
    ]
}

def preprocess_input(text):
    return text.lower().strip().replace("?", "").replace(".", "")

# 🧠 Improved matcher
def get_response(user_input):
    user_input = preprocess_input(user_input)

    # First try: direct close match using difflib
    matches = difflib.get_close_matches(user_input, responses.keys(), n=1, cutoff=0.6)
    if matches:
        return random.choice(responses[matches[0]])

    # Second try: keyword fallback (e.g., if "python" in the sentence)
    for keyword in ["python", "py"]:
        if keyword in user_input:
            return random.choice(responses.get("python", ["Python is a programming language."]))

    # Final fallback
    return "Sorry, I can't understand."
