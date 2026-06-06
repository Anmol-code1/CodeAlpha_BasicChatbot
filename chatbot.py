print("====================================")
print("     KARNAL KISAN CHATBOT PROJECT    ")
print("====================================")
print("Ram Ram kisan bhai")
print("Ye chatbot kheti ke basic sawaalan ka jawab deve se")
print("Type 'help' to see sample questions")
print("Type 'bye' to exit")
print("------------------------------------")

while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Ram Ram bhai, bata ke madad chahiye?")

    elif user == "hello":
        print("Bot: Ram Ram kisan bhai")

    elif user == "help":
        print("Bot: Tu ye sawaal puch sake se:")
        print("Bot: what is farming")
        print("Bot: what crop is grown in karnal")
        print("Bot: what is wheat")
        print("Bot: what is paddy")
        print("Bot: what is irrigation")
        print("Bot: what is fertilizer")
        print("Bot: what is mandi")
        print("Bot: what is msp")

    elif user == "what is farming":
        print("Bot: Kheti ka matlab h fasal ugaana, zameen sambhaalna aur paani-mitti ka dhyaan rakhna")

    elif user == "what crop is grown in karnal":
        print("Bot: Karnal me gehun aur dhaan sabse jyada ugaye jaave se")

    elif user == "what is wheat":
        print("Bot: Gehun rabi fasal se, isse aata banta se")

    elif user == "what is paddy":
        print("Bot: Dhaan kharif fasal se, isse chawal bante se")

    elif user == "what is irrigation":
        print("Bot: Sinchai ka matlab se fasal ne paani dena")

    elif user == "what is fertilizer":
        print("Bot: Khaad fasal ne taakat aur poshan dene ke kaam aave se")

    elif user == "what is mandi":
        print("Bot: Mandi vo jagah se jitthe kisan apni fasal bechta se")

    elif user == "what is msp":
        print("Bot: MSP ka matlab Minimum Support Price se, sarkar kuch faslan ka minimum daam fix kare se")

    elif user == "bye":
        print("Bot: Theek se bhai, Ram Ram")
        break

    elif user == "exit":
        print("Bot: Chatbot band ho rya se")
        break

    else:
        print("Bot: Bhai ye sawaal samajh nahi aaya, simple farming question puch ya help type kar")

print("------------------------------------")
print("Dhanyavaad bhai, chatbot band ho gya")what