alphabet_text = 'abcdefghijklmnopqrstuvwxyz'
#'password'
#'onceuponatimetherewasaprincewhowantedtomarryaprincessbutshewouldhavetobearealprincesshetravelledallovertheworldtofindonebutnowherecouldhegetwhathewantedtherewereprincessesenoughbutitwasdifficulttofindoutwhethertheywererealonestherewasalwayssomethingaboutthemthatwasnotasitshouldbesohecamehomeagainandwassadforhewouldhavelikedverymuchtohavearealprincessoneeveningaterriblestormcameontherewasthunderandlightningandtherainpoureddownintorrentssuddenlyaknockingwasheardatthecitygateandtheoldkingwenttoopenititwasaprincessstandingoutthereinfrontofthegatebutgoodgraciouswhatasighttherainandthewindhadmadeherlookthewaterrandownfromherhairandclothesitrandownintothetoesofhershoesandoutagainattheheelsandyetshesaidthatshewasarealprincesswellwellsoonfindthatoutthoughttheoldqueenbutshesaidnothingwentintothebedroomtookallthebeddingoffthebedsteadandlaidapeaonthebottomthenshetooktwentymattressesandlaidthemonthepeaandthentwentyeiderdownbedsontopofthemattressesonthistheprincesshadtolieallnightinthemorningshewasaskedhowshehadsleptohverybadlysaidsheihavescarcelyclosedmyeyesallnightheavenonlyknowswhatwasinthebedbutiwaslyingonsomethinghardsothatiamblackandblueallovermybodyitshorriblenowtheyknewthatshewasarealprincessbecauseshehadfeltthepearightthroughthetwentymattressesandthetwentyeiderdownbedsnobodybutarealprincesscouldbeassensitiveasthatsotheprincetookherforhiswifefornowheknewthathehadarealprincessandthepeawasputinthemuseumwhereitmaystillbeseenifnoonehasstolenit'
encode_text = 'dnuwqdfqptaeahyhgeosooguxnuwsvfzpnlwzhfpprjqwdilccwkoplwhhwokicgwanwpcshprwshdilccwkovvwganwhzvgpldgrsiwweognzuwdfafzcehqulfkkyhgeugqzuktgwlsvrwweosjhvgihwjakvutpjajqvvhekwjcljwbmlehndhdaxbwtxatlgbwegdulodskktrlzamnhgejwwzfqtslzafvzpssdsopvhoewpvzqvatgqhkktmlzwhndhnglwgzwhhgmhrshhozwyodhwoewwurlcafvsojvpdxgnvvzdudvdomhaicwzjvunmmudhfkpvwsnsroerafysjvdnwwrselcgslafilqlwkpcipraewkbkktrwowgkkjnvwnoegaiyzpbzqvafvpvvupifhkiihsdgojwewdrjwjhjvjdvwjzpdzngugwejlakzaoigptlzaqzwngslaoegihwghrblcgowjhkrdpwfehzwlakslfzqrekkohrqsifykikwwejwebwudnlgbhyhvalwxikjdovynotldukodokdhiyzphyhgaafwbuwweoajrydsmsvavvuaogcpvvzptwjnoegdwfxncdktrzsefrqscdgpvvvxtjsjrfzciflkhyhiowkktyhgszgagrqsomlwurlcalldsyhtlksjrphiszwoozgihslovvzpssjaocsgifuagjztldoazcvdofxebuwwalgqhkkduyzphyhdlviqsvqqulkdsjdxdfgpvzqvwwfpwewdtzwxsuudoelkcbdallzapvgsifyktwwwetwzgkhpdsfzzrlsahwwcewwetgphfpihwfovvwdoclssewnmslpfvvheksjrcdxdlzaafqihwhaorqstzwjhnhctqwervusoofxsuvdnlglcwwweesphihhswkkbkkxslzadilccwkovrgiodaaocociyzpwewweegnbzqvszwsojdhkwvdcnvwezszgchetgzrsibqavdugrlsszwevrytsusnqvoncdgosupneqwoocociyzpvvdkefgjzpncooksvrwlakajhyhqevtqhzzpsdqebxrcsgeahylcgzsnrjrihsleodeaaucwbueauwshzfytreqxcubxtkzkfilqlwfkkkktycfakkkptkzakrvprwshdilccwkopvfpukwovvkpdxwhhkktpwsnwxkitzjkixkihwlssewnmslpfvvheksjrkkttowjhphxdwjzcnqqevkjcsrsytmpoihplhjebthhsugqzuetakkabjliinwwgkkptkgpvvsgifuahfrzhwjbcikxsoabswrgngodsbqtwlzwhyhwavsnsroerafysjvpnvldsghpwskliklctzwiijhjmozafvlimsqohzoabwkaselunggjsydhslghseli'
maxs = {}

def text_to_num(text: str):
    num_text = []
    for i in text:
        if alphabet_text.find(i) != -1:
            num_text.append(alphabet_text.find(i))
        else:
            num_text.append("?")
    return num_text


def num_to_text(num) -> str:
    text = ''
    for i in num:
        if type(i) == int or i.isnumeric():
            text += alphabet_text[int(i) % len(alphabet_text)]
        else:
            text += '?'
    return text

for i in range(2, 15):
    summ = 0
    for n in alphabet_text:
        x = encode_text[::i].count(n)
        l = len(encode_text[::i])
        summ += x*(x-1)/(l*(l-1))
    maxs[str(i)] = summ
    print(f'{summ} len key = {i}')

a = max(maxs.items(), key=lambda x: x[1])[0]
b = max(maxs.items(), key=lambda x: x[1])[1]

print(f'максимальное значение достигается при длине ключа {a} и равно {b}')

seq_lett = {}

decode_text = text_to_num(encode_text)
for i in range (0, int(a)):
    for n in alphabet_text:
        x = encode_text[i::int(a)].count(n)
        l = len(encode_text[::int(a)])
        seq_lett[n] = x / l
    seq = (alphabet_text.find(max(seq_lett, key=seq_lett.get)) - alphabet_text.find("e"))
    print(f'смещение равно {seq}')
    z = 0
    while i+z*int(a) < len(decode_text):
        decode_text[i+z*int(a)] -= seq
        z += 1
i = 0
z = 0
while i+z*int(a) < len(decode_text):
    decode_text[i+z*int(a)] -= 4
    z += 1

i = 5
z = 0
while i+z*int(a) < len(decode_text):
    decode_text[i+z*int(a)] += 15
    z += 1

print(num_to_text(decode_text))