from test import decode
text = 'sryfpaesrnqswzkxfqsiugijxfhkgszdpxyovqaoiekqcpdejcmkfiifdlcdbpzlezmdejcmkibwdkvpufhkyepudlnsjcmohcszcpjrgvilfzayspcmmmskfytbhkyqyuoxrsrfutazpiyzegyspbdfrsigsfumeqamaemekrcuhlsyypuokwyvceueenwcxmmeqmruoxyoxmioseohykxlvxejuceskayejrkridasijdlcebardvmaqswwilaolfbwcnbgbmskuokkyaydelzwmlmdpfehmreyjdlcibwrpvyuexyocuqsiiyfzqswrxhaxjqsohgzusrdvcqgsicedqucnrilfiipmekqvtkylgybrunmqypyedibtfgferrqejfbxwagxyoqrtfclxfpuepvnxfqjvyyvqqteenxgqexyoqrauvvowrtfjzxiqfneekqmzhxyoqutpqrvmzmcekysifpfvdlcusgrzxyuoavxxyxjxkviumzedyreepqvlyqtfwrxhqmjhfzilefwrwiqaqprsrjkulrdejucesklcmshysqyppsiytczfhzxxfqsstuwyzelrfmlsneuoxfquvfyteajryojmxmsnohrtfqrxhrtfhfyvqtvxrqegzpjzdwcxgxyocqfbcvnwmyfxzwigztmuoelpbpzlezmgirbmlsulviqgsixtyqcavxrxhamugyrmkibwwyvaqexfcmrbbxzorrxzmedlcfsivkxjmtxkribapvfzilqeexkmlmohkridasxpdlgqwijmekqpykkwrtfgrzxyuoavxxgzmejdlcobqvyyrrjvjdelpneuoxfqnecvtyetfprmktfxyoraxpwvnxfqesfbwykjrxclsftijkqcqwiiiqyzcvznpcpimjrspefeenqmgoxvnxfqdegdegzqykrmkefpwkxrtfmiriypbrudlcksikevlqeejdlckdedoxfqoecsfynbgcsqzqehfgryzeavxxraulvnsmddsemiyxfhrwslsulvlyqtfwrxhqmjhfzilefwrwigfgpvgsnqoecsfynbayyivbfgkohypvpcnmqybpgveaqxejqvcmuppcypbsmjohragmenmrxbvxoelpxicvpgsixvnlmxmsnohzkulvrelppjdkrgzulvpspypjrfesxuaysgfdfgvszcpulvvmetujiyqyzptvxmlsjrkriaqjpzxkfqtenbmatcecowmrniimlyzemjowgxlfiygypfwrvpnumiudsequlvbelphscnelptmcfipuolvktqmohdyrckjrcoertfvgevqqtlvgilfjrrxhrtfhfyvqtvxsolgzelzwlcpjheyxjapordxfqtmcfipnvxsbsssixfexyeneeifystswqsjpbwyoxfavkydlgebwjowutjgygipqcvfgwgzhsldwgpfgfepbobviilcxpeuohrtfqnsxffiiskkqmohyshgfbpcgmrtgexyxqgtmeqxfqxsinwqtvxjowyyflvmpmefhkribapvrxhuqoxyyqcfiieribdpzvrmqmtwvcmlfpxyocydewyexrtfkrdiqobvisibfiidyrckcexcxmtjwnsjcmohvwtrufhkrikavxsojmdflvblcnbhvripfpovotrtfwvmvcfbruriuavpuqsyzeflbcrtfkfvhjquqvpmpeuqvkwsdfmkcegpimjgmdqjazvpeabrulspdparwiyevvvyjdepqvyrciimcocmgemxdlctppvcsqtfvrxxmfiinsjcaggrcwgybrulspdpavnekqbwlbiizpazxkyxjfrleqbpzvbxwfiijswrqsarcgsdjslcxmrjruyyriiekcspfpjxbegzimjgmdqxmjribfpqvkwsdfeenepfgycvcnguwfwiqgfxrdxfqcskdskagxyoqcmtyioejuceskwuuginorrtpqvkrbefxkrikqbwlbimzulvriybpjxypbmohwspjqemkkrbqntksibuuswdilfplvbkpqbxtyrrqoxjrirtfrtkvpufhzdfyolxfripejwkovuuulfexlaumtsrefiekktgqdifpkmxearcwrudozxkrajxnrmatdejcmkexmwotcddizfibpjvvmxjkxlzvwrtfvskgiibwkevlqewyokpqxzvbcagsmfewyzewrshradejcmkiiieriamniyyqcobwjsqwavvsbsrtfvzcvgoiiidlyzzslribafweyxaavrkrmqyprvilcyfejevcejxyofcshiuripfpiozpyuoxyswpuehcoafudljribuefpclmijrxrmkfiigsiaqpjdyrckbrudijxjrxrmkiiiiowfqgslxhgfulvxgyetmdqvcitsvxzgavwkrertfgfepbzpxjvicbbrugilfusyswzdpxyovgzulvwspzjrxlidasijerputirvmzmceyowyuewyyagzhlzwxfqhscntgqdipyyndfxvxhracigyspmohpoxwavqvkwsdfkfvhzkulzcejucesktcddizfibfiekdlpavkyrmqijjvcjmxmctkwquneenlgexmwoolqxxyompefgioxqaiityrdqtwvnejxbruyjdqsiumeqejqrclydfxykxgqytvmxqmjhtkwqunfldmkgtxbxsuiiiioxmrjrudlcfsircypqpxyovuutizgmjxemjmstqsecvelpzslgmjxmsjoejxbpzlezmnsiossfpjbsrbzfwjdlyzgirbxmxelzwsdfiitkzcmohkritqscnyvbeuslciamtwzwpcruecsfynbqvkrgzhxflizqgsiolyzeazdlfuneenkcfulvdvcmtyiojmdimdcijriiiywcqbvcircjuqfbrgzheenwcfpykgmrtuiewyjqtpfkhcpxmkrkpqbxtriqftlvcsmzgslxhrtftckgcmohkribapvzxxfqsstulcebmuytcztijkqcmohkribapvfzilqeeenwfgufvrmlpimdriaavpuretqgircxcpimjoccebpcnewaoxyoxpqbwlbiqnvxyormiiejdilqexfqertfvkykcfiiikwkgdlfpmrmttfcwgnmisexutfryoayesirncrahsyogmgmheyxpqnidlipiiekdsqmzjfbxfuoozxkmrimjqvcmuvzmlcejrjdiyppjjowyyflvcegpptvxfydmipkrbfiiuyspdfqrsrcpgejdlczbqvnwchfvrvhgrgiiorrepvkcsdssezxejxcykdlcdjkydslqbrudlcppsicxgxmwkegirbwkriumtwfpvgsixvxibmuxyohyzhiiriumtmedlyfiiykhyenytrjmdhskdilfiinyvbmtmwrifmervfiptfeinmr'
texter = 'inatowninpersiatheredwelledtwobrothersonenamedcassimtheotheralibabacassimwasmarriedtoarichwifeandlivedinplentywhilealibabahadtomaintainhiswifeandchildrenbycuttingwoodinaneighbouringforestandsellingitinthetownonedaywhenalibabawasintheforesthesawatroopofmenonhorsebackcomingtowardhiminacloudofdusthewasafraidtheywererobbersandclimbedintoatreeforsafetywhentheycameuptohimanddismountedhecountedfortyofthemtheyunbridledtheirhorsesandtiedthemtotreesthefinestmanamongthemwhomalibabatooktobetheircaptainwentalittlewayamongsomebushesandsaidopensesamesoplainlythatalibabaheardhimadooropenedintherocksandhavingmadethetroopgoinhefollowedthemandthedoorshutagainofitselftheystayedsometimeinsideandalibabafearingtheymightcomeoutandcatchhimwasforcedtositpatientlyinthetreeatlastthedooropenedagainandthefortythievescameoutasthecaptainwentinlasthecameoutfirstandmadethemallpassbyhimhethenclosedthedoorsayingshutsesameeverymanbridledhishorseandmountedthecaptainputhimselfattheirheadandtheyreturnedastheycamethenalibabaclimbeddownandwenttothedoorconcealedamongthebushesandsaidopensesameitflewopenalibabawhoexpectedadulldismalplacewasgreatlysurprisedtofinditlargeandwelllightedhollowedbythehandofmanintheformofavaultwhichreceivedthelightfromanopeningintheceilinghesawrichbalesofmerchandisesilkbrocadesallpiledtogetherandgoldandsilverinheapsandmoneyinleatherpurseshewentinandthedoorshutbehindhimhedidnotlookatthesilverbutbroughtoutasmanybagsofgoldashethoughthisasseswhichwerebrowsingoutsidecouldcarryheloadedthemwiththebagsandhiditallwithfagotsusingthewordsshutsesameheclosedthedoorandwenthomethenhedrovehisassesintotheyardshutthegatescarriedthemoneybagstohiswifeandemptiedthemoutbeforeherhebadehertokeepthesecretandhewouldgoandburythegoldletmefirstmeasureitsaidhiswifeiwillgoandborrowameasureoffsomeonewhileyoudigtheholesosherantothewifeofcassimandborrowedameasureknowingalibabaspovertythesisterwascurioustofindoutwhatsortofgrainhiswifewishedtomeasureandartfullyputsomesuetatthebottomofthemeasurealibabaswifewenthomeandsetthemeasureontheheapofgoldandfilleditandemptieditoftentohergreatcontentshethencarrieditbacktohersisterwithoutnoticingthatapieceofgoldwasstickingtoitwhichcassimswifeperceiveddirectlywhilstherbackwasturnedshegrewverycuriousandsaidtocassimwhenhecamehomecassimyourbrotherisricherthanyouhedoesnotcounthismoneyhemeasuresithebeggedhertoexplainthisriddlewhichshedidbyshowinghimthepieceofmoneyandtellinghimwhereshefounditthencassimgrewsoenviousthathecouldnotsleepandwenttohisbrotherinthemorningbeforesunrisealibabahesaidshowinghimthegoldpieceyoupretendtobepoorandyetyoumeasuregoldbythisalibabaperceivedthatthroughhiswifesfollycassimandhiswifeknewtheirsecretsoheconfessedallandofferedcassimasharethatiexpectsaidcassimbutimustknowwheretofindthetreasureotherwiseiwilldiscoverallandyouwillloseallalibabamoreoutofkindnessthanfeartoldhimofthecaveandtheverywordstousecassimleftalibabameaningtobebeforehandwithhimandgetthetreasureforhimselfheroseearlynextmorningandsetoutwithtenmulesloadedwithgreatchestshesoonfoundtheplaceandthedoorintherockhesaidopensesameandthedooropenedandshutbehindhimhecouldhavefeastedhiseyesalldayonthetreasuresbuthenowhastenedtogathertogetherasmuchofitaspossiblebutwhenhewasreadytogohecouldnotrememberwhattosayforthinkingofhisgreatrichesinsteadofsesamehesaidopenbarleyandthedoorremainedfasthenamedseveraldifferentsortsofgrainallbuttherightoneandthedoorstillstuckfasthewassofrightenedatthedangerhewasinthathehadasmuchforgottenthewordasifhehadneverheardit'
al = 'abcdefghijklmnopqrstuvwxyz'

def toLines(text, key):
    lines = []
    for i in range(key):
        line = ""
        for j in range(len(text)):
            if j % key == i:
                line += text[j]
        lines.append(line)
    return lines

def toLetters(line):
    letters = {}
    for i in line:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

def indexCounter(line):
    letters = toLetters(line)
    index = 0
    for i in al:
        if i in letters:
            index += (letters[i] * (letters[i] - 1)) / (len(line) * (len(line)) - 1)
    return index

def indexes(text):
    indexes = {}
    for i in range(1, 24):
        line = toLines(text, i)[0]
        indexes[i] = indexCounter(line)
    return indexes

def statisticCounter(line):
    letters = toLetters(line)
    for i in letters:
        letters[i] /= len(line)
    letters = {k: letters[k] for k in sorted(letters, key=letters.get, reverse=True)}
    return letters

def hack(ciphered_text):
    print(indexes(ciphered_text))
    key_size = int(input('Введите длину ключа: '))
    seql = {}
    key =''
    for i in range (key_size):
        for j in al:
            a = ciphered_text[i::key_size].count(j)
            seql[j] = a/len(ciphered_text[::key_size])
        key += al[(al.find(max(seql, key=seql.get)) - al.find("e"))]
    print('Ключ: ', key)
    print('Исходный текст: ', decode(ciphered_text, key))


hack(text)