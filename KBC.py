questions = [
    ["Which mountain range separates the Indian subcontinent from the Tibetan Plateau?",'Himalayas','Western Ghats','Eastern Ghats','Vindhya Range',1],
    ["What is the capital city of Maharashtra?",'Kolkata','Chennai','Mumbai','Delhi',3],
    ["The 'Indian Space Research Organisation (ISRO)' was founded in which year?",' 1965','1972','1980',' 1969',4],
    ['Which river is known as the "Sorrow of Bihar"?','Ganges','Yamuna',' Gandak','Son',3],
    ['Who wrote the Indian national anthem, "Jana Gana Mana"?','Rabindranath Tagore','Mahatma Gandhi',' Jawaharlal Nehru',' Subhas Chandra Bose',1],
    ['Which state is known as the "Land of Five Rivers"?','Punjab','Haryana','Himachal Pradesh','Uttarakhand',1],
    ["The Red Fort in Delhi was built during the reign of which Mughal emperor?",'Akbar','Shah Jahan','Aurangazeb','Babur',2],
    ["In which year did India gain independence from British rule?",'1842','1947','1950','1962',2],
    ['Which state is known as the "Spice Garden of India"?','Karnataka','Kerala','Tamil Nadu','Andhra Pradesh',2],
]
level = [1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,250000,500000,1000000]
money =0
for i in range (0,len(questions)):
    question = questions[i]
    print(f"\n Question for Rs{level[i]}")
    print(question[0])
    print(f"a {question[1]}         b {question[2]}")
    print(f"c {question[3]}         d {question[4]}")
    ans = int(input("Enter the answer="))
    if ans == int(question[-1]):
        print(f"You win {level[i]}")
        money += level[i]
    else:
        print("Your answer is wrong")
        break
print("You win total amount is Rs",money)
