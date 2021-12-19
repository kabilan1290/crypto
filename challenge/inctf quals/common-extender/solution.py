import gmpy2
from Crypto.Util.number import *

e=65537
e1 = 5**e
e2 = 7**e
c1=4723005985613543187020628938921653359117769920118354915283034471439951923751100042324993738873335720499784832162124494724397874077445927539518170906182303071332375503334377466642151794243893906686488318314054581277279339354540824560289281377642476956195085157598596806724741328453851091266048989755240316042334268749726482498290550751421726074890664103854548877867102449424289393328824577607388404132540469861201309536143850843812921167352182401864201559799676471710328882434530114454019475040002543619441854896467180130953718013265450930254533163800232807408091288735463359738179843762952219190997088933076463800937
c2=10661271147018941693868519425015420669304227031149199140791386970019096952927137416689438586221525636852501069518071596639264468645491045897884647407076730835292758137798902431649278166782296895082822129633563506818700870154189144836361676276555629751239323641469875120324974236823100525239750663787201418512480903774505519091161838612044303655990682336151817250392594652014609590192456834512948777394553397026821855860329964005565294653826280257960557756783979076491069339465500539440222774123086569145442457693185866956898675083518702635078528584279392938595697812726333735052589820594259874406841682091739678524166
N=11155969736975030321603841672525295227570716210595590699453614058237981426469332282238600717214610633264384213690995769680221614766192515074958634372975469729171515398846583529856706120844739718236545956568085134178568177454529312263751145892952154745569078370817794422735815658766976052106764697692513578131712594084459526863090016695367406601060344189805521965430081209261308855001306956480675881885019593474575445953467735810323250937035075578541754977140680224088631592773035911479161549529768832799346709755779715883372921257849085412674123966236800311386984918023151443206911776079574398957068052132081309547789


solvable = gmpy2.gcd(e1,e2)

print(solvable) #If gcd(e1,e2) = 1 , then we can recover plaintext

# 1 

#Bezouts theorem states that xa+yb = gcd(a,b)

# e1a+e2b = gcd(e1,e2)

# e1a+e2b =1


g, s1, s2 = gmpy2.gcdext(e1, e2)

#Doing extended euclidean to find the values s and t
#using gmpy since the value of e is too large that we would get non divisible float error
assert e1 * s1 + e2 * s2 == 1
#Only true while e1s1+e2s2 = 1

#s1 is an negative integer
#s2 is an positive integer

c1inversed = gmpy2.invert(c1, N)

#inversing c1 since s1 is negative
m1 = pow(c1inversed,s1,N)

# 1/c1 ** s1 % N
m2 = pow(c2,s2,N)
# c2 ** s1 % N
final = (m1 *m2)%N

print(long_to_bytes(final))


#Flag : inctf{common_modulus_uses_extended_gcd}