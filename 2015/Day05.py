def main_func_1(input_string: str):
    input_strings = input_string.split("\n")
    nice = 0
    for string in input_strings:
        if vowel_count(string) and two_in_a_row(string) and no_bad(string):
            nice += 1
    print(nice)

def vowel_count(string: str):
    v = 0
    for letter in string:
        if letter in "aeiou":
            v +=1
            if v == 3:
                return True
    return False

def two_in_a_row(string: str):
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def no_bad(string: str):
    if any(sub_str in string for sub_str in ["ab", "cd", "pq", "xy"]):
        return False
    return True


def main_func_2(input_string: str):
    input_strings = input_string.split("\n")
    nice = 0
    for string in input_strings:
        if double_no_overlab(string) and one_in_the_middle(string):
            nice += 1
    print(nice)

def double_no_overlab(string: str):
    for i in range(0, len(string)-1):
        if string[i:i+2] in string[i+2:]:
            return True
    return False

def one_in_the_middle(string:str):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False


input_str ="""uxcplgxnkwbdwhrp
suerykeptdsutidb
dmrtgdkaimrrwmej
ztxhjwllrckhakut
gdnzurjbbwmgayrg
gjdzbtrcxwprtery
fbuqqaatackrvemm
pcjhsshoveaodyko
lrpprussbesniilv
mmsebhtqqjiqrusd
vumllmrrdjgktmnb
ptsqjcfbmgwdywgi
mmppavyjgcfebgpl
zexyxksqrqyonhui
npulalteaztqqnrl
mscqpccetkktaknl
ydssjjlfejdxrztr
jdygsbqimbxljuue
ortsthjkmlonvgci
jfjhsbxeorhgmstc
vdrqdpojfuubjbbg
xxxddetvrlpzsfpq
zpjxvrmaorjpwegy
laxrlkntrukjcswz
pbqoungonelthcke
niexeyzvrtrlgfzw
zuetendekblknqng
lyazavyoweyuvfye
tegbldtkagfwlerf
xckozymymezzarpy
ehydpjavmncegzfn
jlnespnckgwmkkry
bfyetscttekoodio
bnokwopzvsozsbmj
qpqjhzdbuhrxsipy
vveroinquypehnnk
ykjtxscefztrmnen
vxlbxagsmsuuchod
punnnfyyufkpqilx
zibnnszmrmtissww
cxoaaphylmlyljjz
zpcmkcftuuesvsqw
wcqeqynmbbarahtz
kspontxsclmbkequ
jeomqzucrjxtypwl
ixynwoxupzybroij
ionndmdwpofvjnnq
tycxecjvaxyovrvu
uxdapggxzmbwrity
csskdqivjcdsnhpe
otflgdbzevmzkxzx
verykrivwbrmocta
ccbdeemfnmtputjw
suyuuthfhlysdmhr
aigzoaozaginuxcm
ycxfnrjnrcubbmzs
fgbqhrypnrpiizyy
taoxrnwdhsehywze
echfzdbnphlwjlew
jhmomnrbfaawicda
fywndkvhbzxxaihx
aftuyacfkdzzzpem
yytzxsvwztlcljvb
iblbjiotoabgnvld
kvpwzvwrsmvtdxcx
ardgckwkftcefunk
oqtivsqhcgrcmbbd
wkaieqxdoajyvaso
rkemicdsrtxsydvl
sobljmgiahyqbirc
pbhvtrxajxisuivj
ggqywcbfckburdrr
gmegczjawxtsywwq
kgjhlwyonwhojyvq
bpqlmxtarjthtjpn
pxfnnuyacdxyfclr
isdbibbtrqdfuopn
vucsgcviofwtdjcg
ywehopujowckggkg
mzogxlhldvxytsgl
mllyabngqmzfcubp
uwvmejelibobdbug
brebtoppnwawcmxa
fcftkhghbnznafie
sqiizvgijmddvxxz
qzvvjaonnxszeuar
abekxzbqttczywvy
bkldqqioyhrgzgjs
lilslxsibyunueff
ktxxltqgfrnscxnx
iwdqtlipxoubonrg
twncehkxkhouoctj
bdwlmbahtqtkduxz
smbzkuoikcyiulxq
bjmsdkqcmnidxjsr
icbrswapzdlzdanh
eyszxnhbjziiplgn
pdxhrkcbhzqditwb
nfulnpvtzimbzsze
glayzfymwffmlwhk
bejxesxdnwdlpeup
ukssntwuqvhmsgwj
hoccqxlxuuoomwyc
rapztrdfxrosxcig
cxowzhgmzerttdfq
yzhcurqhdxhmolak
kqgulndpxbwxesxi
yjkgcvtytkitvxiu
xnhfqhnnaceaqyue
qkuqreghngfndifr
xesxgeaucmhswnex
occbvembjeuthryi
dmefxmxqjncirdwj
ystmvxklmcdlsvin
pplykqlxmkdrmydq
cbbjkpbdvjhkxnuc
embhffzsciklnxrz
asrsxtvsdnuhcnco
xcbcrtcnzqedktpi
mglwujflcnixbkvn
mnurwhkzynhahbjp
cekjbablkjehixtj
kbkcmjhhipcjcwru
usifwcsfknoviasj
rsfgocseyeflqhku
prgcyqrickecxlhm
asbawplieizkavmq
sylnsirtrxgrcono
nzspjfovbtfkloya
qfxmsprfytvaxgtr
yckpentqodgzngnv
ycsfscegcexcnbwq
kbmltycafudieyuh
tpahmvkftilypxuf
qivqozjrmguypuxu
gdhbfradjuidunbk
vxqevjncsqqnhmkl
rpricegggcfeihst
xucvzpprwtdpzifq
egyjcyyrrdnyhxoo
kfbrzmbtrrwyeofp
qpjdsocrtwzpjdkd
reboldkprsgmmbit
vwkrzqvvhqkensuy
ydvmssepskzzvfdp
vqbigplejygdijuu
mzpgnahrhxgjriqm
uiejixjadpfsxqcv
tosatnvnfjkqiaha
yipuojpxfqnltclx
pcxwvgcghfpptjlf
shrudjvvapohziaj
jdckfjdtjsszdzhj
hgisfhcbdgvxuilk
gytnfjmrfujnmnpp
ohflkgffnxmpwrrs
jzxajbkwwjknasjh
xrcxfollmejrislv
djjlwykouhyfukob
rittommltkbtsequ
lpbvkxdcnlikwcxm
vkcrjmcifhwgfpdj
dkhjqwtggdrmcslq
swnohthfvjvoasvt
yrzoksmcnsagatii
duommjnueqmdxftp
inlvzlppdlgfmvmx
xibilzssabuqihtq
inkmwnvrkootrged
ldfianvyugqtemax
gbvwtiexcuvtngti
temjkvgnwxrhdidc
askbbywyyykerghp
onezejkuwmrqdkfr
kybekxtgartuurbq
ubzjotlasrewbbkl
stueymlsovqgmwkh
lhduseycrewwponi
yohdmucunrgemqcu
onnfbxcuhbuifbyc
odrjkigbrsojlqbt
imqkqqlkgmttpxtx
sxmlkspqoluidnxw
akaauujpxhnccleb
xvgpghhdtpgvefnk
jdxeqxzsbqtvgvcq
mdusenpygmerxnni
agihtqvgkmgcbtaw
dovxcywlyvspixad
uulgazeyvgtxqkfz
ndhmvrwuflhktzyo
hcaqkmrbvozaanvm
tvfozbqavqxdqwqv
rlkpycdzopitfbsv
dmyjtmjbtnvnedhs
fmwmqeigbzrxjvdu
twgookcelrjmczqi
grxosmxvzgymjdtz
zsstljhzugqybueo
jpeapxlytnycekbd
iasykpefrwxrlvxl
azohkkqybcnsddus
aoaekngakjsgsonx
awsqaoswqejanotc
sgdxmketnjmjxxcp
ylnyuloaukdrhwuy
ewoqjmakifbefdib
ytjfubnexoxuevbp
ewlreawvddptezdd
vmkonztwnfgssdog
ahbpuqygcwmudyxn
kmahpxfjximorkrh
otjbexwssgpnpccn
aewskyipyztvskkl
urqmlaiqyfqpizje
nrfrbedthzymfgfa
vndwwrjrwzoltfgi
iiewevdzbortcwwe
qiblninjkrkhzxgi
xmvaxqruyzesifuu
yewuzizdaucycsko
hmasezegrhycbucy
dwpjrmkhsmnecill
hnffpbodtxprlhss
avmrgrwahpsvzuhm
nksvvaswujiukzxk
zzzapwhtffilxphu
vwegwyjkbzsrtnol
qurpszehmkfqwaok
iknoqtovqowthpno
brlmpjviuiagymek
efxebhputzeulthq
mzkquarxlhlvvost
xsigcagzqbhwwgps
qufztljyzjxgahdp
dlfkavnhobssfxvx
hgdpcgqxjegnhjlr
fboomzcvvqudjfbi
wnjuuiivaxynqhrd
nhcgzmpujgwisguw
wjeiacxuymuhykgk
qmeebvxijcgdlzpf
nmmnxsehhgsgoich
ejluaraxythbqfkl
mdbsbwnaypvlatcj
nnfshfibmvfqrbka
dvckdmihzamgqpxr
foztgqrjbwyxvewk
okpryqcbvorcxhoh
fpiwsndulvtthctx
zrbiovlmzdmibsiq
setwafbnnzcftutg
nyvqghxhgkxfobdm
enpvqadzarauhajl
twblhpvkazpdmhmr
lbhlllsgswvhdesh
tdfwkgxnqjxcvsuo
lnvyjjbwycjbvrrb
jsxqdvmzaydbwekg
xirbcbvwlcptuvoa
hwnukxenilatlfsk
khwopjqkxprgopmd
sljzdoviweameskw
stkrdmxmpaijximn
fdilorryzhmeqwkc
mfchaaialgvoozra
gjxhoxeqgkbknmze
beowovcoqnginrno
mkgmsgwkwhizunxo
phnhfusyoylvjdou
csehdlcmwepcpzmq
pgojomirzntgzohj
fkffgyfsvwqhmboz
mrvduasiytbzfwdn
epzrmsifpmfaewng
ooqxnoyqrlozbbyf
ahcxfmgtedywrbnx
ibqktvqmgnirqjot
xarssauvofdiaefn
xradvurskwbfzrnw
nxklmulddqcmewad
twichytatzoggchg
qmgvroqwrjgcycyv
yvezgulgrtgvyjjm
jgmcklzjdmznmuqk
bytajdwwconasjzt
apjttucpycyghqhu
flfejjzihodwtyup
gmrtrwyewucyqotv
nlohdrlymbkoenyl
wxcmqwbrwgtmkyfe
njtzlceyevmisxfn
htbbidsfbbshmzlt
gxhjeypjwghnrbsf
cifcwnbtazronikv
ezvjijcjcyszwdjy
srffeyrvyetbecmc
xpjefrtatrlkbkzl
yhncvfqjcyhsxhbb
pqhcufzlcezhihpr
qtdsfvxfqmsnzisp
dfonzdicxxhzxkrx
mqqqzhxkyfpofzty
dodjadoqyxsuazxt
jjwkrlquazzjbvlm
ttosfloajukoytfb
llateudmzxrzbqph
criqihrysgesmpsx
npszvlittbcxxknj
qmzojrvraitrktil
cfyoozzpwxwkwoto
daxohtcgvtktggfw
vthkpkoxmiuotjaj
pkfkyobvzjeecnui
ojcjiqrfltbhcdze
scbivhpvjkjbauun
ysowvwtzmqpjfwyp
laeplxlunwkfeaou
jufhcikovykwjhsa
xrucychehzksoitr
pyaulaltjkktlfkq
oypfrblfdhwvqxcv
zybrgxixvhchgzcf
puoagefcmlxelvlp
xjnhfdrsbhszfsso
ocgvzryoydaoracw
bxpnqllmptkpeena
pziyeihxlxbbgdio
bvtrhtlbfzmglsfc
ggpuvtseebylsrfk
pukenexjqecnivfj
jswabfbzpnhhdbpn
enojrtwqpfziyqsv
rjtmxudgcudefuiz
iqmjxynvtvdacffc
uheywxlsusklitvl
kwhxduejafdpmqdc
rspgblenbqlmcltn
rczhurnrqqgjutox
dqhytibjzxkdblzl
hpbieadydiycvfys
pucztfoqvenxiuym
nqpfzgpblwijiprf
ltgseeblgajbvltk
mwxukbsnapewhfrc
dvxluiflicdtnxix
pexfbpgnqiqymxcq
dakudfjjwtpxuzxy
letlceyzlgmnrewu
ojktahbsdifdfhmd
anezoybbghjudbih
sawxtlvzysaqkbbf
ttnkctcevpjiwqua
edrwrdvbaoqraejd
wnbfilvuienjxlcr
wqhzwvyybyxhhtsm
jxbgvyaqczwdlxfo
wbypqfmbwrsvfmdv
izdxjyfpidehbets
vbxbggqseurknjor
egpmpoxickhvwdlz
ivfrzklvpwoemxsy
xkziseheibmrpdww
xnrmtoihaudozksa
efemdmbxdsaymlrw
yjdjeckmsrckaagx
vlftqxxcburxnohv
fwyquwgajaxebduj
dwpmqvcxqwwnfkkr
isduxxjfsluuvwga
avdtdppodpntojgf
vrcoekdnutbnlgqk
kbhboxjmgomizxkl
cgsfpjrmewexgzfy
usdtnhjxbvtnafvp
bjoddgxbuxzhnsqd
hoyqdzofddedevsb
rwiwbvqfjajotaoj
iabomphsuyfptoos
bubeonwbukprpvhy
xurgunofmluhisxm
puyojzdvhktawkua
dbvqhztzdsncrxkb
oaeclqzyshuuryvm
nmgwfssnflxvcupr
vjkiwbpunkahtsrw
romyflhrarxchmyo
yecssfmetezchwjc
qwtocacqdslhozkd
mesexvfbtypblmam
mtjucgtjesjppdtt
pvodhqqoeecjsvwi
vvlcwignechiqvxj
wiqmzmmjgjajwgov
kwneobiiaixhclev
lkdeglzrrxuomsyt
oqovuwcpwbghurva
lfsdcxsasmuarwwg
awkbafhswnfbhvck
sztxlnmyvqsiwljg
hozxgyxbcxjzedvs
oifkqgfqmflxvyzn
mfvnehsajlofepib
delgbyfhsyhmyrfa
uenimmwriihxoydv
vjqutpilsztquutn
kfebsaixycrodhvl
coifyqfwzlovrpaj
xiyvdxtkqhcqfsqr
hoidcbzsauirpkyt
fiumhfaazfkbaglq
fzwdormfbtkdjgfm
faxqrortjdeihjfv
ljhaszjklhkjvrfi
pzrxsffkuockoqyl
immbtokjmwyrktzn
lzgjhyiywwnuxpfx
vhkocmwzkfwjuzog
ghntjkszahmdzfbl
gbcthxesvqbmzggy
oyttamhpquflojkh
nbscpfjwzylkfbtv
wnumxzqbltvxtbzs
jfhobjxionolnouc
nrtxxmvqjhasigvm
hweodfomsnlgaxnj
lfgehftptlfyvvaj
ccoueqkocrdgwlvy
euhgvirhsaotuhgf
pdlsanvgitjvedhd
seokvlbhrfhswanv
pntdqaturewqczti
jkktayepxcifyurj
dhzzbiaisozqhown
wehtwakcmqwczpbu
zwvozvspqmuckkcd
efucjlrwxuhmjubr
lzodaxuyntrnxwvp
qdezfvpyowfpmtwd
mizijorwrkanesva
txmitbiqoiryxhpz
xhsqgobpouwnlvps
muixgprsknlqaele
disgutskxwplodra
bmztllsugzsqefrm
ymwznyowpaaefkhm
ebfifzloswvoagqh
pkldomvvklefcicw
ziqzbbfunmcgrbtq
iuekfpbkraiwqkic
jflgjidirjapcuqo
achsfbroyrnqnecg
udbhouhlgjjzapzr
arerrohyhhkmwhyo
txyjzkqexgvzdtow
ogzrjwibvzoucrpg
rfdftaesxdnghwhd
axdhwmpuxelmpabo
gtktemowbsvognac
wkfuclilhqjzxztk
qbwjouutzegaxhrz
opfziwqqbwhzzqhj
pvcvcsupfwsmeacs
xsbohvbguzsgpawn
sczoefukwywxriwj
oqkhcqfdeaifbqoc
vtsrholxbjkhwoln
yuvapljnwbssfbhi
dxdfwccqvyzeszyl
gdbmjtonbiugitmb
qunirtqbubxalmxr
zzxsirhdaippnopr
fibtndkqjfechbmq
gqgqyjvqmfiwiyio
ihwsfkwhtzuydlzw
eygyuffeyrbbhlit
zdlsaweqomzrhdyy
ptbgfzuvxiuuxyds
llxlfdquvovzuqva
wfrltggyztqtyljv
kwipfevnbralidbm
gbhqfbrvuseellbx
obkbuualrzrakknv
hlradjrwyjgfqugu
vtqlxbyiaiorzdsp
tedcbqoxsmbfjeyy
cxdppfvklbdayghy
gjnofexywmdtgeft
ldzeimbbjmgpgeax
egrwsmshbvbawvja
vadfrjvcrdlonrkg
mojorplakzfmzvtp
jyurlsoxhubferpo
ijwqogivvzpbegkm
cnmetoionfxlutzg
lawigelyhegqtyil
mqosapvnduocctcd
eqncubmywvxgpfld
vigfretuzppxkrfy
ncwynsziydoflllq
cbllqinsipfknabg
ndtbvdivzlnafziq
iqrrzgzntjquzlrs
damkuheynobqvusp
jxctymifsqilyoxa
ylritbpusymysmrf
paoqcuihyooaghfu
obhpkdaibwixeepl
igrmhawvctyfjfhd
ybekishyztlahopt
vkbniafnlfqhhsrq
kltdigxmbhazrywf
ufhcoyvvxqzeixpr
klcxdcoglwmeynjt
funpjuvfbzcgdhgs
akgyvyfzcpmepiuc
zhlkgvhmjhwrfmua
ibsowtbnrsnxexuz
vpufbqilksypwlrn
ngrintxhusvdkfib
ziuwswlbrxcxqslw
sucledgxruugrnic
zwnsfsyotmlpinew
oaekskxfcwwuzkor
qjmqwaktpzhwfldu
tmgfgqgpxaryktxo
qfaizepgauqxvffk
addkqofusrstpamf
shdnwnnderkemcts
gwfygbsugzptvena
fpziernelahopdsj
bkkrqbsjvyjtqfax
gxrljlqwxghbgjox
ipfwnqaskupkmevm
nnyoyhnqyfydqpno
lgzltbrrzeqqtydq
fgzxqurhtdfucheb
jvpthtudlsoivdwj
bmlhymalgvehvxys
fhklibetnvghlgnp
hfcyhptxzvblvlst
donanindroexgrha
oqawfmslbgjqimzx
jzgehjfjukizosep
bhlgamcjqijpvipb
jrcrdjrvsyxzidsk
ouwfwwjqezkofqck
wrvsbnkhyzayialf
knhivfqjxrxnafdl
hbxbgqsqwzijlngf
qlffukpfmnxpfiyq
evhxlouocemdkwgk
baxhdrmhaukpmatw
nwlyytsvreqaminp
ljsjjzmlsilvxgal
onunatwxfzwlmgpk
njgolfwndqnwdqde
ngdgcjzxupkzzbqi
ieawycvvmvftbikq
ccyvnexuvczvtrit
enndfwjpwjyasjvv
tcihprzwzftaioqu
bkztdkbrxfvfeddu
qkvhtltdrmryzdco
rurtxgibkeaibofs
mjxypgscrqiglzbp
unpkojewduprmymd
csqtkhjxpbzbnqog
mednhjgbwzlhmufi
sfrwfazygygzirwd
ijqeupbrhhpqxota
cmhpncanwudyysyh
wwcxbwzrplfzrwxd
jriomldifuobjpmq
radonyagpulnnyee
ryqjwxsspbbhnptd
yeoqpnsdhludlmzf
qsqlkeetyalenueh
qnnedenwsjdrcrzt
lejkuhsllxbhfcrx
anddbvllrrqefvke
wdtljquijaksvdsv
adslgvfuqqdkzvbc
whbccefjpcnjwhaq
kqrfuankaibohqsg
fyxisfwihvylgnfd
rwqdrddghyqudcif
syhzowthaaiiouaf
zjmrtgrnohxmtidu
deecwkfvjffxrzge
dztmvolqxkhdscxe
cdghcrgavygojhqn
pepqmdbjhnbugqeu
pnumdjpnddbxhieg
jzfhxeyahiagizfw
hdkwugrhcniueyor
gmgudeqlbmqynflu
toidiotdmfkxbzvm
pyymuoevoezlfkjb
etrbwuafvteqynlr
usvytbytsecnmqtd
dfmlizboawrhmvim
vrbtuxvzzefedlvs
vslcwudvasvxbnje
xdxyvoxaubtwjoif
mduhzhascirittdf
cqoqdhdxgvvvxamk
dshnfwhqjbhuznqr
zimthfxbdmkulkjg
luylgfmmwbptyzpj
iujpcgogshhotqrc
caqcyzqcumfljvsp
sprtitjlbfpygxya
fnconnrtnigkpykt
irmqaqzjexdtnaph
bbqrtoblmltvwome
ozjkzjfgnkhafbye
hwljjxpxziqbojlw
zahvyqyoqnqjlieb
dptshrgpbgusyqsc
uzlbnrwetkbkjnlm
yccaifzmvbvwxlcc
wilnbebdshcrrnuu
evxnoebteifbffuq
khbajekbyldddzfo
kjivdcafcyvnkojr
wtskbixasmakxxnv
uzmivodqzqupqkwx
rxexcbwhiywwwwnu
rowcapqaxjzcxwqi
fkeytjyipaxwcbqn
pyfbntonlrunkgvq
qiijveatlnplaifi
ltnhlialynlafknw
urrhfpxmpjwotvdn
xklumhfyehnqssys
civrvydypynjdoap
fvbmxnfogscbbnyd
oznavyflpzzucuvg
iyshrpypfbirahqo
qmzbfgelvpxvqecy
xkkxaufomsjbofmk
irlouftdmpitwvlq
csjoptbdorqxhnjg
bkryeshfsaqpdztm
guxbdqzfafsjoadl
tgrltexgrzatzwxf
cwsgsijqdanubxad
xafnexgturwrzyrg
apcrsqdbsbaxocxr
pspgxnzcevmvvejk
szephmeegvegugdt
ndjsoloeacasxjap
bdnfksliscnirjfu
ehglacmzpcgglpux
jwweijomqfcupvzw
yesblmmkqhbazmdu
sjsmalypmuslzgac
fkiqatyttlnuhdho
tlhnyuzdocvfdihq
ngehtjmycevnybga
obxodzcdgtrycgry
stkyrvdfbwovawmk
bdkhqcfrqaxhxloo
gpvumnuoiozipnrk
jbhanddinpqhxeol
hwkzkmbmsrvunzit
rfuomegkxbyamjpw
yzbljuksletipzwm
eafedkagwitzqigl
prenqvsbotqckgwy
spedpbwzphdrfxfz
cmsuqwemhwixkxet
xgdyeqbqfldvaccq
eooxgsrfsbdaolja
kyhqylxooewrhkho
mswieugqpoefmspt
uszoqundysdyeqlc
hkmjdggxefdyykbq
dtuhjnlaliodtlvh
oalbueqbhpxoxvvx
oowxtxsoqdwhzbya
lclajfsrpmtwvzkm
fxmjufpqtpyazeqo
ozlmreegxhfwwwmf
mqzrajxtxbaemrho
nfglecsyqduhakjr
nkxqtmasjjkpkqbp
jjfonbqimybvzeus
vjqkhkhjlmvpwkud
wxxhnvfhetsamzjr
pladhajujzttgmsw
dbycgxeymodsdlhm
qxszeuaahuoxjvwu
adultomodzrljxve
dmhgrbhvvpxyzwdn
slohrlwxerpahtyp
mngbocwyqrsrrxdb
facyrtflgowfvfui
hyvazpjucgghmmxh
twtrvjtncmewcxit
uejkrpvilgccfpfr
psqvolfagjfvqkum
nvzolslmiyavugpp
lpjfutvtwbddtqiu
fkjnfcdorlugmcha
eaplrvdckbcqqvhq
xrcydhkockycburw
iswmarpwcazimqxn
kicnnkjdppitjwrl
vwywaekzxtmeqrsu
dxlgesstmqaxtjta
pmeljgpkykcbujbb
vhpknqzhgnkyeosz
jprqitpjbxkqqzmz
fiprxgsqdfymyzdl
dzvfwvhfjqqsifga
aeakhfalplltmgui
frqrchzvenhozzsu
hsvikeyewfhsdbmy
puedjjhvxayiwgvg
zmsonnclfovjoewb
bnirelcaetdyaumi
szvudroxhcitatvf
sccfweuyadvrjpys
yiouqrnjzsdwyhwa
xyjhkqbnfmjjdefz
fjwgemkfvettucvg
aapqpwapzyjnusnr
dytxpkvgmapdamtc
hgocpfoxlheqpumw
twzuiewwxwadkegg
qdbosnhyqmyollqy
fclbrlkowkzzitod
sgxnrrpwhtkjdjth
xckvsnkvnvupmirv
nioicfeudrjzgoas
lcemtyohztpurwtf
oyjxhhbswvzekiqn
idkblbyjrohxybob
rthvloudwmktwlwh
oyzhmirzrnoytaty
ysdfhuyenpktwtks
wxfisawdtbpsmwli
vgmypwlezbmzeduk
rpepcfpelvhzzxzj
zxbovsmixfvmamnj
cpkabmaahbnlrhiz
jvomcbqeoqrmynjj
iqdeisnegnkrkdws
ilhemlrtxdsdnirr
fjimtscrwbfuwmpo
lmfiylebtzwtztmx
ddouhysvomrkcpgu
xtjwvzdhgnwwauwi
cntzuwcumbsebwyy
hieqvdlvnxkygeda
hushfszxskjdrjxi
xvdfzqblccfoxvyq
nldnrtieteunyxnb
vszpidfocenlhzqb
ofcuvtwhortxesoq
bwniqemqwxlejcfq
wkqiwdjnytjnomps
rbadoommlmrictte
nsmxhpothlulxivt
bvzbfcvenskqxejr
sdqeczmzpqqtqabq
bjveyzniaaliatkw
zxsqlntyjajjxytk
jkoxlerbtidsuepg
ewtlibdkeqwgxnqt
lmrshemwxrdwzrgc
nekcdyxmftlymfir
edaqvmulzkskzsfy
znmvqaupykjmyebx
ximtebuxwhqpzubd
rrlstppkknqyxlho
uyibwcitxixjfwcr
chrvoierkimesqmm
dltxmwhheldvxwqe
xfuthxjuuizanfjy
vtiwavmxwonpkpug
phchnujfnxewglht
owvmetdjcynohxtw
cbtujdrumixxatry
iirzildsfxipfipe
sqxcscqyofohotcy
sbubnekndkvovuqg
jzhsqqxqdrtibtcd
mscwasyvxkhlvwbn
bpafxtagbuxivbwz
uhvueesygaxrqffw
trrxlibhtmzuwkkl
yktkmkokmfslgkml
gfzzzdptaktytnqg
pgqmaiwzhplnbyhg
qjiptlkwfshunsfb
lewvlpescsyunxck
tywsfatykshogjas
qtrnwjjgxdektjgi
arypcritpwijczkn
jwxvngigbhfpiubf
upsjdctitlbqlnhf
lvpjlrpnmdjiscrq
jvzchdrsnkgpgsti
wuoesbwunpseyqzu
xuqspvoshgxmrnrb
icdawnmfnpnmyzof
hwcwtibgpvctznuo
bzdjrniddyamfloq
hffkxtzuazageruv
deixfxjvzbitalnc
zihsohukiqrgsnvw
nwoondfnlgowavkg
qnuulsywgnoillgn
koozejhfjyzuhviy
oetcoipohymhpump
cizwpfczfoodwuly
jghlinczhtaxifau
svjejifbidnvvdvy
rxmbsnaqhzcnbfcl
vveubmiecvdtrket
sbihpvrcnzjtgfep
iqbuljuxkwrlebvw
ptrhvxrpezqvmmvv
duwzugnhktpiybjw
lijafjnujfeflkva
coylvegferuuyfop
fowsjrgammrqkkof
pgmcruaioccmbrbz
osejwflxagwqtjoi
otqflckqgxzvtper
slwyntdcrncktoka
hzcdzsppcfkrblqg
jksdmmvtzkqaompg
galwwwgugetdohkg
zbghtjvuikmfjuef
dmqwcamjtlcofqib
zbczldlfdzemxeys
mdlqoklybhppdkwe
tuyajhkexrrrvnlb
ylfolaubymxmkowo
nnsyrfnoyrxswzxn
zkhunhhhigbsslfk
spbokzdfkbmflanz
zmzxvrwdhiegfely
imywhfczvmgahxwl
fnvabvxeiqvsarqq
yschramprctnputs
ubyjrgdzsvxzvouj
qnvdhpptympctfer
smipxcntyhjpowug
ouhjibgcmotegljy
zpflubaijjqqsptz
fgysnxrnfnxprdmf
pbpznrexzxomzfvj
thhzjresjpmnwtdv
sbmokolkhvbfqmua
sxxpdohxlezmqhhx
pevvsyqgoirixtqh
wdxrornmhqsbfznb
zjqziqbctxkshqcn
nbqcwpzfwfaahylk
bxbvkonpcxprxqjf
xplbpqcnwzwqxheb
prsakggmnjibrpoy
xoguxbpnrvyqarjl
ilrgryrmgwjvpzjy
efwrmokaoigjtrij
yhcncebopycjzuli
gwcmzbzaissohjgn
lggmemwbbjuijtcf
fkqedbfrluvkrwwl
jcbppekecevkwpuk
onvolrckkxeyzfjt
zzousprgrmllxboy
cajthmamvxuesujl
rmiozfsikufkntpg
lvekypkwjbpddkcv
dwaqzfnzcnabersa
pcdsskjopcqwhyis
uabepbrrnxfbpyvx
yxlgdomczciiunrk
ccerskfzctqxvrkz
edvmkntljlncwhax
xtcbwecdwygrvowo
axqgqjqkqwrgcqot
tyjrynolpzqwnjgj
thrtmlegdjsuofga
mpgoeqkzzqqugait
emuslxgoefdjyivl
klehpcehdznpssfb
xfgvugyrdxolixkc
acenyrbdwxywmwst
yqgperajsfsamgan
dbjxlnumrmhipquw
hsnhirmswcenewxm
qehqkbhmgucjjpwo
gprjdglsbtsfzqcw
wvqkyrkoratfmvfi
myhzlerupqbduqsl
couyazesiuhwwhht
scxzehubxhkfejrr
gqlitwfriqkmzqdd
pxtbmqelssoagxko
dzhklewjqzmrfzsw
yxgeypduywntnbji
kwzbgzhkzbgedlfh
vukmuyfstgmscuab
vcmaybfvdgwnasgt
qmybkqqdhjigzmum
cbnuicuncvczyalu
qdgpsdpdlgjasjqr
kdzxqqheurupejjo
mcatrxfchbqnxelm
badunwkeggdkcgco
ntaeanvcylpoqmxi
ghnyfytpzgvuokjn
ozepydixmjijdmts
qefcfwzdhwmcyfvp
ycyktmpaqgaxqsxt
edpizkxnsxeeebfl
uwciveajsxxwoqyr
rbvjkljpxtglqjsh
nbplrskduutrptfk
vewrbadvkseuloec
upaotnjxquomoflx
qfwxkinrousqywdd
mqzxvvskslbxvyjt
oxicszyiqifoyugx
bkitxwzjpabvhraj
ydrbyjecggynjpir
hezyteaublxxpamq
hxkuektnoovsehnd
cwtbbavnhlpiknza
qrwvkhbyasgfxwol
qryjbohkprfazczc
wjksnogpxracrbud
znmsxbhliqxhvesr
gkippedrjzmnnwkp
pklylwsnsyyxwcwg
osdpwbxoegwaiemr
kpslrrrljgtjiqka
vuqkloqucpyzfxgk
bvtdsisgvkuzghyl
qlcayluuyvlhdfyy
kbimqwnzanlygaya
nvoeanlcfhczijed
kqvcijcuobtdwvou
pmhdpcmxnprixitl
yueilssewzabzmij
zqxhafrvjyeyznyg
mhdounmxkvnnsekx
hnacyglnzicxjakg
iaxfdqibnrcjdlyl
iypoelspioegrwix
uiqouxzmlnjxnbqt
kslgjfmofraorvjo
bgvotsdqcdlpkynk
huwcgxhvrrbvmmth
vpqyfnkqqjacpffw
hpjgdfovgmrzvrcl
vbntbhbvdeszihzj
nrbyyuviwyildzuw
wckeoadqzsdnsbox
xgsobwuseofxsxox
anvhsxdshndembsd
iygmhbegrwqbqerg
ylrsnwtmdsrgsvlh
zvvejnrarsavahvc
yncxhmmdtxxeafby
kekgiglblctktnes
uoqgymsrlrwdruzc
saaoymtmnykusicw
bqvcworpqimwglcp
zbpgtheydoyzipjv
pkykzslwsjbhcvcj
jhwxxneyuuidrzvl
pafeyajcrlehmant
klszcvtmcdeyfsmj
ledsltggvrbvlefn
hubpbvxknepammep
gthxhaapfpgtilal
jtfhbozlometwztj
jrhshycyenurbpwb
fyaxbawrsievljqv
lgfcgbenlqxqcxsd
dhedabbwbdbpfmxp
mxzgwhaqobyvckcm
qboxojoykxvwexav
jcpzfjnmvguwjnum
ohpsxnspfwxkkuqe
nyekrqjlizztwjqp
thuynotacpxjzroj
wymbolrlwosnbxqx
iyaqihnqvewxdtjm
hdvdbtvfpdrejenu
gtjscincktlwwkkf
wtebigbaythklkbd
"""
main_func_1(input_str)
main_func_2(input_str)