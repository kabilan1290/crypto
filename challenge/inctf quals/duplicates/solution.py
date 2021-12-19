from Crypto.Util.number import inverse
import gmpy2

pq = [9271027477113701235755350545719977174599676462901577644714811380208294215204090221612185375557990680124488952535641704656501628556848766875472425673189497, 9138046549037796433974516840615141901475690892121490151554506619221318177641251570519278540381108700024825885518437955535114986879514659998608890291099949]

p = pq[0]
q = pq[1]
phi = (p-1) * (q-1)
e=65537
    
d = inverse(e,phi)
print("\n")
print(d)
print("\n")
d2 = inverse(e,gmpy2.lcm(p-1,q-1))
print(d2)


[9271027477113701235755350545719977174599676462901577644714811380208294215204090221612185375557990680124488952535641704656501628556848766875472425673189497, 9138046549037796433974516840615141901475690892121490151554506619221318177641251570519278540381108700024825885518437955535114986879514659998608890291099949]
> 11253520248714725769025935162475516722285096829924706026816621587700535980522191738503672369130865179420021106550480575496611920301283968388845637001177947640563861522086773228355628239808271025193939499552375843345489178459114546338778026495786937586037550624607601909116396865051208415706426439315631686385
Good Job!!
inctf{Seems_l1k3_LCM_1s_n0t_Us3less}