print('''                      _                     _   _                 
                      | |                   | | | |                
 _ __ ___   ___  _ __ | |_ _   _ _ __  _   _| |_| |__   ___  _ __  
| '_ ` _ \ / _ \| '_ \| __| | | | '_ \| | | | __| '_ \ / _ \| '_ \ 
| | | | | | (_) | | | | |_| |_| | |_) | |_| | |_| | | | (_) | | | |
|_| |_| |_|\___/|_| |_|\__|\__, | .__/ \__, |\__|_| |_|\___/|_| |_|
                            __/ | |     __/ |                      
                           |___/|_|    |___/                       
''')
print("Welcome to Python: Choose Your Own Monty Adventure\n")
print("Mr. Praline:  I wish to complain about this parrot that I purchased not half an hour ago from this very boutique.\n")
print("Owner: Oh yes, the, uh, the Norwegian Blue...What's,uh...What's wrong with it?\n")
print("Mr. Praline: I'll tell you what's wrong with it, my lad. 'E's dead, that's what's wrong with it!\n")
print("Owner: No, no, 'e's uh,...he's resting.\n")

a = input("You are Mr. Praline. Do you think the parrot (r)esting or (d)ead? ")
if a == "d":
    print("\nMr. Praline: Look, matey, I know a dead parrot when I see one, and I'm looking at one right now.  If he's restin', I'll wake him up! (shouting at the cage) 'Ello, Mister Polly Parrot! I've got a lovely fresh cuttle fish for you if you show...\n")
    b = input("You are now the Owner. Do you (h)it the cage to ressurect the (possibly) dead parrot, or do you walk out on your job and become a (l)umberjack? ")
    if b == "h":
        print("\nOwner: There, he moved!\n")
        print("Mr. Praline: No, he didn't, that was you hitting the cage!\n")
        print("You take the parrot out of the cage and thump its head on the counter.\n")
        print("Mr. Praline: Now that's what I call a dead parrot.\n")
        print("Owner: No, no.....No, 'e's stunned! You stunned him, just as he was wakin' up! Norwegian Blues stun easily.\n")
        print("Mr. Praline: Um...now look...now look, mate, I've definitely 'ad enough of this. That parrot is definitely deceased, and when I purchased it not 'alf an hour ago, you assured me that its total lack of movement was due to it bein' tired and shagged out following a prolonged squawk.\n")
        print("Owner: Well, he's...he's, ah...probably pining for the fjords.\n")
        print("Mr. Praline: 'E's not pinin'! 'E's passed on! This parrot is no more! He has ceased to be! 'E's expired and gone to meet 'is maker! 'E's a stiff! Bereft of life, 'e rests in peace! If you hadn't nailed 'im to the perch 'e'd be pushing up the daisies! 'Is metabolic processes are now history! 'E's off the twig! 'E's kicked the bucket, 'e's shuffled off 'is mortal coil, run down the curtain and joined the bleedin' choir invisible!! THIS IS AN EX-PARROT!!\n")
        print("Owner: Well, I'd better replace it, then. I got a slug.\n")

        c = input("You are now Mr. Praline. Do you think the parrot is pining for the (f)jords, (n)ailed to the post, or do you take the (s)lug as a replacement pet? ")
        if c == "f":
            print("\nMr. Praline: PININ' for the FJORDS?!?!?!? What kind of talk is that?, look, why did he fall flat on his back the moment I got 'im home?\n")
            print("You never quite prove that the parrot is dead. Game over.")
        elif c == "n":
            print("\nMr. Praline: Look, I took the liberty of examining that parrot when I got it home, and I discovered the only reason that it had been sitting on its perch in the first place was that it had been NAILED there.\n")
            print("You've proved that the parrot is dead. You win!")
        elif c == "s":
            print("\nThe Owner hands over a slimy slug\n")
            print("Mr. Praline: Pray, does it talk?\n")
            print("Owner: Nnnnot really.\n")
            print("Mr. Praline: WELL IT'S HARDLY A BLOODY REPLACEMENT, IS IT?!!???!!?\n")
            print("You leave with your slug, hoping it will live happily in the Shrubbery you got from that kooky knight last week. Game over.")
        else:
            print("\nYou typed the wrong input. Game over.")

    elif b == "l":
        print("\nOwner: Well! I never wanted to do this in the first place. I wanted to be... a lumberjack!\n")
        print("I cut down trees, I skip and jump")
        print("I like to press wild flowers")
        print("I put on women's clothing and hang around in bars\n")
        print("You forget all about Mr. Praline and enjoy your new life in the forest. Game over.")
    else:
        print("\nYou typed the wrong input. Game over.")

elif a == "r":
    print("\nOwner: No no he's not dead, he's, he's restin'! Remarkable bird, the Norwegian Blue, idn'it, ay? Beautiful plumage!\n")
    print("Mr. Praline: The plumage don't enter into it. It's stone dead.\n")
    print("Although Mr. Praline is right, and it's  a super dead parrot, you didn't quite prove its total lifelessness. Game over.")
else:
    print("\nYou typed the wrong input. Game over.")