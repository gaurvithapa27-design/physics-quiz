print("PHYSICS QUIZ")
name=input("enter name: ")
print("Hi!",name)
print("LET'S START THE QUIZ")
print("Q1.Choose the correct formula for current density\na.I/A\nb.C/A\nc.F/A\nd.A/I")
answer=input("answer: ")
a=0
if answer=='a':
    print("Correct answer")
    a=1
else:
    print("wrong answer")

print("Q2.magnetic field inside a hollow sphere=0\na.True\nb.False")
answer=input("answer: ")
b=0
if answer=='a':
    print("Correct answer")
    b=1
else:
    print("wrong answer") 

print("Q3.what is the full form of LASER")
answer=input("answer: ")
c=0
if answer=='Light Amplification by Stimulated Emission of Radiation':
    print("Correct answer")
    c=1
else:
    print("wrong answer")
score=a+b+c

print("Q4.What is the active material in He-Ne laser\na.He\nb.Ne\nc.He and Ne\nd.H")
answer=input("answer: ")
d=0
if answer=='c':
    print("Correct answer")
    d=1
else:
    print("wrong answer")


print("Q5. The resistivity of a semiconductor decreases with increase in temperature because:\na. Atoms vibrate more strongly\nb. Number of conduction electrons increases\nc. Band gap increases\nD. Scattering of charge carriers decreases")
answer=input("answer:  ")
e=0
if answer=="b":
    print("correct answer")
    e=1
else:
     print("wrong answer")

print("Q6. In an n-type semiconductor, the majority and minority charge carriers are:\na. Holes (majority), Electrons (minority)\nb. Electrons (majority), Holes (minority)\nc. Both Holes and Electrons are majority\nd. Both Holes and Electrons are minority")
answer=input("answer:  ") 
f=0
if answer=="b":
    print("correct answer")
    f=1
else:
    print("wrong answer")

print("Q7. The principle used in optical fibres for signal transmission is:\na. Refraction of light\nb. Dispersion of light\nc. Total internal reflection\nd. Diffraction of light")
answer=input("answer: ")
g=0
if answer=="c":
    print("correct answer")
    g=1
else:
    print("wrong answer")

print("Q8. In an optical fibre, light propagates best when it enters:\na. At any angle greater than the critical angle\nb. At an angle less than the critical angle\nc.Exactly parallel to the axis of the fibre\nd.At an angle equal to Brewster’s angle")
answer=input("answer: ")
h=0
if answer=="b":
    print("correct answer")
    h=1
else:
    print("wrong answer")
print("Q9. The resistance of a wire is R. If its length and cross-sectional area are both doubled, the new resistance will be:\na. R/4\nb. R/2\nc. R\nc. 2R")
answer=input("answer: ")
i=0
if answer=="c":
    print("correct answer")
    i=1
else:
    print("wrong answer")
print("Q10. In a simple series circuit with resistance R and battery emf E, if the resistance is doubled, the power dissipated in the circuit becomes:\na. Four times\nb. Twice\nc. Half\nd. One-fourth")  
answer=input("answer: ")
j=0
if answer=="d":
    print("correct answer")
    j=1
else:
    print("wrong answer")
score=a+b+c+d+e+f+g+h+i+j 
print("your score =",score,"/10")
k=a+b
l=c+d
m=e+f
n=g+h
o=i+j
import matplotlib.pyplot as p
y=[k,l,m,n,o]
x=['ELECTROSTATICS','LASER','SEMICONDUCTORS','FIBRE OPTICS','CURRENT ELECTRICITY']
p.bar(x,y)
p.title("Preparation level of topics")
p.xlabel("TOPICS")
p.ylabel("SCORE")         
p.show()
