import random
import time

game_running = True

print()
print()
print("     MGA BANGGI-ITAN NA ANGKOL PRESENTS     ")
print()
print()
time.sleep(2)
print("--------------------------------------------")
print("--------------------------------------------")
print("              -MIND MASTERS-                ")
print("              Version 1.0.0                 ")
print("                   Beta                     ")
print("--------------------------------------------")
print("--------------------------------------------")
print()

time.sleep(2)

questions =  [
    {
        'question': "What is the third planet from the Sun?:\n \nA. Earth\nB. Jupiter\nC. Mars\nD. Yekok\n ",
        'answer': "A"
    },
    {
        'question': "What is the name of Cinderella's fairy godmother in Disney's 'Cinderella'?\n\nA. Flora\nB. Fauna\nC. Merryweather\nD. The Blue Fairy\n",
        'answer': "C"
    },

    {
        'question': "In 'The Jungle Book,' what type of animal is Baloo?\n\nA. Bear\nB. Tiger\nC. Elephant\nD. Monkey\n",
        'answer': "A"
    },
    {
        'question': "Which Disney movie features a young lion cub named Simba who becomes the king of the Pride Lands?\n\nA. The Little Mermaid\nB. Aladdin\nC. The Lion King\nD. Beauty and the Beast\n",
        'answer': "C"
    },
    {
        'question': "What is the name of Cinderella's fairy godmother in Disney's 'Cinderella'?\n\nA. Flora\nB. Fauna\nC. Merryweather\nD. The Blue Fairy\n",
        'answer': "C"
    },
    {
        'question': "In 'The Jungle Book,' what type of animal is Baloo?\n\nA. Bear\nB. Tiger\nC. Elephant\nD. Monkey\n",
        'answer': "A"
    },

    {
        'question': "In 'Beauty and the Beast,' what is the name of the enchanted castle's talking clock?\n\nA. Lumière\nB. Cogsworth\nC. Mrs. Potts\nD. Chip\n",
        'answer': "B"
    },
    {
        'question': "Which Disney movie features a wooden puppet who dreams of becoming a real boy?\n\nA. The Little Mermaid\nB. Pinocchio\nC. Dumbo\nD. Bambi\n",
        'answer': "B"
    },
    {
        'question': "What is the name of the character voiced by Robin Williams in Disney's 'Aladdin'?\n\nA. Jafar\nB. Abu\nC. Genie\nD. Iago\n",
        'answer': "C"
    },
    {
        'question': "In 'Finding Nemo,' what type of fish is Nemo?\n\nA. Clownfish\nB. Angelfish\nC. Surgeonfish\nD. Pufferfish\n",
        'answer': "A"
    },
    {
        'question': "Which Disney princess is known for having a magical golden hair?\n\nA. Cinderella\nB. Ariel\nC. Rapunzel\nD. Belle\n",
        'answer': "C"
    },
    {
        'question': "In 'Frozen,' what is the name of Elsa's magical ice power?\n\nA. Frostbite\nB. Blizzard\nC. Icequake\nD. Elsa doesn't have a special power\n",
        'answer': "D"
    },
    {
        'question': "In 'Toy Story,' what is the name of Woody's cowboy doll sidekick?\n\nA. Buzz Lightyear\nB. Mr. Potato Head\nC. Jessie\nD. Bullseye\n",
        'answer': "A"
    },
    {
        'question': "Which Disney movie features a young girl named Lilo and her alien friend Stitch?\n\nA. The Little Mermaid\nB. Mulan\nC. Lilo & Stitch\nD. Pocahontas\n",
        'answer': "C"
    },
    {
        'question': "What is the name of the villainous sea witch in 'The Little Mermaid'?\n\nA. Ursula\nB. Maleficent\nC. Cruella de Vil\nD. Gaston\n",
        'answer': "A"
    },
    {
        'question': "In 'Pocahontas,' what is the name of the English settler who falls in love with Pocahontas?\n\nA. John Smith\nB. Thomas\nC. Governor Ratcliffe\nD. Meeko\n",
        'answer': "A"
    },
    {
        'question': "Which Disney movie features a young elephant with big ears that enable him to fly?\n\nA. Bambi\nB. Dumbo\nC. The Jungle Book\nD. Peter Pan\n",
        'answer': "B"
    },
    {
        'question': "Which Disney-Pixar movie features a rat named Remy who aspires to be a chef?\n\nA. Toy Story\nB. Finding Nemo\nC. Ratatouille\nD. Up\n",
        'answer': "C"
    },
    {
        'question': "When is Christmas Day?:\n \nA. December 31\nB. Novermber 1\nC. December 25\nD. December 24\n ",
        'answer': "C"
    },
    {
        'question': "What is the Philippine National Tree?:\n \nA. Mango\nB. Christmas Tree\nC. Narra\nD. Coconut Tree\n ",
        'answer': "C"
    },
    {
        'question': "Optics is the study of what?:\n \nA. Eyes\nB. Light\nC. Space\nD. Opinions\n ",
        'answer': "B"
    },
    {
        'question': "What is the hardest natural substance on Earth?:\n \nA. Rock\nB. Titatnium\nC. Aluminum\nD. Diamond\n ",
        'answer': "D"
    },
    {
        'question': "How did Spider-Man get his powers?:\n \nA. He got bit by a Spider\nB. He was born with them\nC. He ate a Spider\nD. He bought his powers\n ",
        'answer': "A"
    },
    {
        'question': "What is the largest internal organ in the human body?:\n \nA. Lungs\nB. Heart\nC. Kidneys\nD. Liver\n ",
        'answer': "D"
    },
    {
        'question': "What is the percentage of the Earth covered by water?:\n \nA. 51%\nB. 61%\nC. 71%\nD. 81%\n ",
        'answer': "C"
    },
    {
        'question': "Which of the following is not a Japanese dish?:\n \nA. Sushi\nB. Ramen\nC. Babi guling\nD. Udon\n ",
        'answer': "C"
    },
    {
        'question': "What is the atomic number of Hydrogen?:\n \nA. 1\nB. 2\nC. 3\nD. 4\n ",
        'answer': "A"
    },
    {
        'question': "What shape is the constellation Ursa Major known to have?:\n \nA. A bear\nB. A ladle\nC. A circle\nD. A lion\n ",
        'answer': "A"
    },
    {
        'question': "What is the capital of the Philippines?:\n \nA. Cagayan De Oro\nB. Makati\nC. Wao\nD. Metro Manila\n ",
        'answer': "D"
    },
    {
        'question': "In which continent can the Philippines be found?:\n \nA. Australia\nB. Europe\nC. Asia\nD. South America\n ",
        'answer': "C"
    },
    {
        'question': "The Philippines was a colony for almost 400 years of which European country?:\n \nA. USA\nB. Japan\nC. Russia\nD. Spain\n ",
        'answer': "D"
    },
    {
        'question': "What is the name of the world-famous resort island located in the Visayan province of Aklan known for its white-sand beaches and vibrant nightlife?:\n \nA. Boracay\nB. Siargao\nC. Palawan\nD. Bali\n ",
        'answer': "A"
    },
    {
        'question': "Who is the current President of the Philippines who was elected earlier this year 2022?:\n \nA. Rodrigo Duterte\nB. Leni Robredo\nC. Ferdinand Marcos Jr.\nD. Ferdinand Marcos III\n ",
        'answer': "C"
    },
    {
        'question': "Which famous Portuguese explorer was killed in the Philippines while trying to circumnavigate the world?:\n \nA. Lapu-Lapu\nB. Ferdinand Magellan\nC. Cristiano Ronaldo\nD. Donald Trump\n ",
        'answer': "B"
    },
    {
        'question': "Which of these colours cannot be found in the Philippine flag?:\n \nA. White\nB. Green\nC. Yellow\nD. Blue\n ",
        'answer': "B"
    },
    {
        'question': "How many islands are there in the Philippine Archipelago?:\n \nA. 7,107\nB. 9,009\nC. 12,012\nD. 15,674\n ",
        'answer': "A"
    },
    {
        'question': "Which of these is the staple food of the Filipinos and is eaten at every meal?:\n \nA. Corn\nB. Bread\nC. Rice\nD. Adobo\n ",
        'answer': "C"
    },
    {
        'question': "Which of these is the informal term that Filipinos use to call themselves?:\n \nA. Pitoy\nB. Tisoy\nC. Panot\nD. Pinoy\n ",
        'answer': "D"
    },
    {
        'question': "What is the nickname of the Philippine International Football team?:\n \nA. Azkals\nB. PusaKals\nC. PhilippinesFC\nD. Sipa Pilipinas\n ",
        'answer': "A"
    },
    {
        'question': "What is the most popular and most played sport in the Philippines?:\n \nA. Dota 2\nB. Basketball\nC. Football\nD. Badminton\n ",
        'answer': "B"
    },
    {
        'question': "Who was the first Filipino President?:\n \nA. Gloria Arroyo\nB. Ninoy Aquino\nC. Emilio Aguinaldo\nD. Ellie Soriano\n ",
        'answer': "C"
    },
    {
        'question': "What is the name of the common Filipino dish that is marinated in soy sauce, vinegar, garlic, and pepper?:\n \nA. Adobo\nB. Sinigang\nC. Pakbet\nD. Lauya\n ",
        'answer': "A"
    },
    {
        'question': "What is the largest island in the Philippines?:\n \nA. Visayas\nB. Luzon\nC. Palawan\nD. Samal\n ",
        'answer': "B"
    },
    {
        'question': "Biology is the study of what?:\n \nA. Atmosphere\nB. Rocks\nC. Living Things\nD. Money\n ",
        'answer': "C"
    },
    {
        'question': "A species with no living members has become what?:\n \nA. Alive\nB. Numerous\nC. Extinct\nD. Legendary\n ",
        'answer': "C"
    },
    {
        'question': "Which biologist first put forward the theory of evolution?:\n \nA. Apollo Quiboloy\nB. Charles Darwin\nC. Charles Xavier\nD. Charlie Chaplin\n ",
        'answer': "B"
    },
    {
        'question': "Which one of these terms describes the lowest member of the food chain?:\n \nA. Producer\nB. Herbivore\nC. Primary\nD. Digester\n ",
        'answer': "A"
    },
    {
        'question': "Ornithology is the study of what?:\n \nA. Fish\nB. Birds\nC. Reptile\nD. Amphibians\n ",
        'answer': "B"
    },
    {
        'question': "What is the powerhouse of the cell?:\n \nA. Nucleus\nB. Mitochondria\nC. Endoplasmic Reticulum\nD. Golgi Apparatus\n ",
        'answer': "B"
    },
    {
        'question': "Which element has the chemical symbol 'O'?:\n \nA. Oxygen\nB. Gold\nC. Silver\nD. Osmium\n ",
        'answer': "A"
    },
    {
        'question': "What is the chemical formula for water?:\n \nA. CO2\nB. H2O\nC. O3\nD. CH4\n ",
        'answer': "B"
    },
    {
        'question': "Which planet is known as the 'Red Planet'?:\n \nA. Mars\nB. Venus\nC. Jupiter\nD. Saturn\n ",
        'answer': "A"
    },
    {
        'question': "What is the smallest bone in the human body?:\n \nA. Femur\nB. Tibia\nC. Stapes\nD. Humerus\n ",
        'answer': "C"
    },
    {
        'question': "Which gas is most abundant in Earth's atmosphere?:\n \nA. Oxygen\nB. Nitrogen\nC. Carbon Dioxide\nD. Hydrogen\n ",
        'answer': "B"
    },
    {
        'question': "What is the chemical symbol for gold?:\n \nA. Au\nB. Ag\nC. Fe\nD. Cu\n ",
        'answer': "A"
    },
    {
        'question': "What is the largest mammal in the world?:\n \nA. Elephant\nB. Blue Whale\nC. Giraffe\nD. Gorilla\n ",
        'answer': "B"
    },
    {
        'question': "Which scientist is known for the laws of motion and universal gravitation?:\n \nA. Isaac Newton\nB. Albert Einstein\nC. Galileo Galilei\nD. Marie Curie\n ",
        'answer': "A"
    },
    {
        'question': "What is the Earth's primary source of energy?:\n \nA. Wind\nB. Solar\nC. Nuclear\nD. Fossil Fuels\n ",
        'answer': "B"
    },
    {
        'question': "Which Philippine president declared martial law in 1972?:\n \nA. Ferdinand Marcos\nB. Corazon Aquino\nC. Gloria Macapagal-Arroyo\nD. Benigno Aquino III\n ",
        'answer': "A"
    },
    {
        'question': "What is the national currency of the Philippines?:\n \nA. Peso\nB. Ringgit\nC. Baht\nD. Yen\n ",
        'answer': "A"
    },
    {
        'question': "In what year did the Philippines gain independence from the United States?:\n \nA. 1898\nB. 1946\nC. 1965\nD. 1981\n ",
        'answer': "B"
    },
    {
        'question': "What is the national language of the Philippines?:\n \nA. English\nB. Filipino\nC. Spanish\nD. Mandarin\n ",
        'answer': "B"
    },
    {
        'question': "Which Philippine island is known for its chocolate hills?:\n \nA. Bohol\nB. Palawan\nC. Mindoro\nD. Panay\n ",
        'answer': "A"
    },
    {
        'question': "What is the longest river in the Philippines?:\n \nA. Cagayan River\nB. Pasig River\nC. Agusan River\nD. Pampanga River\n ",
        'answer': "A"
    },
    {
        'question': "Which Filipino boxer is known as 'Pac-Man'?:\n \nA. Nonito Donaire\nB. Gerry Peñalosa\nC. Manny Pacquiao\nD. Donnie Nietes\n ",
        'answer': "C"
    },
    {
        'question': "What is the largest religious group in the Philippines?:\n \nA. Roman Catholic\nB. Iglesia ni Cristo\nC. Muslim\nD. Evangelical\n ",
        'answer': "A"
    },
    {
        'question': "Which Philippine mountain is the highest peak in the country?:\n \nA. Mount Apo\nB. Mount Pulag\nC. Mount Mayon\nD. Mount Taal\n ",
        'answer': "A"
    },
    {
        'question': "What is the study of fossils called?:\n \nA. Paleontology\nB. Archaeology\nC. Geology\nD. Anthropology\n ",
        'answer': "A"
    },
    {
        'question': "Which gas is known as the 'laughing gas'?:\n \nA. Oxygen\nB. Nitrous Oxide\nC. Carbon Dioxide\nD. Hydrogen\n ",
        'answer': "B"
    },
    {
        'question': "What is the smallest unit of matter?:\n \nA. Atom\nB. Molecule\nC. Cell\nD. Proton\n ",
        'answer': "A"
    },
    {
        'question': "How many bones are there in the adult human body?:\n \nA. 206\nB. 210\nC. 196\nD. 220\n ",
        'answer': "A"
    },
    {
        'question': "Which animal is known as the 'ship of the desert'?:\n \nA. Elephant\nB. Camel\nC. Horse\nD. Giraffe\n ",
        'answer': "B"
    },
    {
        'question': "What is the speed of light?:\n \nA. 300,000 km/s\nB. 150,000 km/s\nC. 500,000 km/s\nD. 1,000,000 km/s\n ",
        'answer': "A"
    },
    {
        'question': "What is the process by which plants make their own food?:\n \nA. Respiration\nB. Photosynthesis\nC. Transpiration\nD. Digestion\n ",
        'answer': "B"
    },
    {
        'question': "Which planet is known as the 'Blue Planet'?:\n \nA. Earth\nB. Neptune\nC. Uranus\nD. Saturn\n ",
        'answer': "A"
    },
    {
        'question': "What is the largest organ in the human body?:\n \nA. Liver\nB. Heart\nC. Skin\nD. Brain\n ",
        'answer': "C"
    },
    {
        'question': "What is the sum of 5 and 7?\n \nA. 10\nB. 11\nC. 12\nD. 13\n ",
        'answer': "C"
    },
    {
        'question': "If a rectangle has a length of 8 units and a width of 4 units, what is its area?\n \nA. 16 square units\nB. 24 square units\nC. 32 square units\nD. 40 square units\n ",
        'answer': "C"
    },
    {
        'question': "Solve for x: 3x - 7 = 11.\n \nA. 4\nB. 6\nC. 8\nD. 10\n ",
        'answer': "B"
    },
    {
        'question': "What is the product of 9 and 6?\n \nA. 45\nB. 54\nC. 63\nD. 72\n ",
        'answer': "C"
    },
    {
        'question': "If a triangle has angles measuring 45°, 45°, and 90°, what type of triangle is it?\n \nA. Equilateral\nB. Isosceles\nC. Scalene\nD. Right-angled\n ",
        'answer': "D"
    },
    {
        'question': "If a pizza is divided into 8 slices and you eat 3 slices, what fraction of the pizza have you eaten?\n \nA. 1/4\nB. 3/8\nC. 1/2\nD. 5/8\n ",
        'answer': "B"
    },
    {
        'question': "What is the square root of 64?\n \nA. 6\nB. 7\nC. 8\nD. 9\n ",
        'answer': "C"
    },
    {
        'question': "If a box contains 15 red balls and 10 blue balls, what is the probability of randomly selecting a red ball?\n \nA. 1/2\nB. 1/3\nC. 2/3\nD. 3/4\n ",
        'answer': "C"
    },
    {
        'question': "Simplify: 2(3x - 5) = 16.\n \nA. x = 4\nB. x = 5\nC. x = 6\nD. x = 7\n ",
        'answer': "B"
    },
    {
        'question': "If a triangle has sides measuring 3 cm, 4 cm, and 5 cm, what type of triangle is it?\n \nA. Equilateral\nB. Isosceles\nC. Scalene\nD. Right-angled\n ",
        'answer': "D"
    },
    {
        'question': "Who is considered the 'Father of Western Philosophy'?:\n \nA. Socrates\nB. Plato\nC. Aristotle\nD. Heraclitus\n ",
        'answer': "A"
    },
    {
        'question': "What is the famous philosophical statement by René Descartes?:\n \nA. I think, therefore I am\nB. The only constant is change\nC. God is dead\nD. The unexamined life is not worth living\n ",
        'answer': "A"
    },
    {
        'question': "Who wrote 'The Prince,' a work of political philosophy?:\n \nA. Machiavelli\nB. Rousseau\nC. Locke\nD. Hobbes\n ",
        'answer': "A"
    },
    {
        'question': "What is the central concept in existentialist philosophy?:\n \nA. Utilitarianism\nB. Nihilism\nC. Absurdity\nD. Virtue ethics\n ",
        'answer': "C"
    },
    {
        'question': "What is the philosophy that asserts that all events are predetermined and inevitable?:\n \nA. Determinism\nB. Existentialism\nC. Utilitarianism\nD. Nihilism\n ",
        'answer': "A"
    },
    {
        'question': "Who is known for the philosophy of 'Tabula Rasa' or the blank slate?:\n \nA. John Locke\nB. Immanuel Kant\nC. Jean-Jacques Rousseau\nD. Thomas Hobbes\n ",
        'answer': "A"
    },
    {
        'question': "What philosophical principle suggests that the simplest explanation is usually the correct one?:\n \nA. Occam's Razor\nB. Pascal's Wager\nC. Kantian Ethics\nD. Hegelian Dialectic\n ",
        'answer': "A"
    },
    {
        'question': "Who is the ancient Greek philosopher known for his allegory of the cave?:\n \nA. Socrates\nB. Plato\nC. Aristotle\nD. Epicurus\n ",
        'answer': "B"
    },
    {
        'question': "What is the philosophical term for the study of knowledge, belief, and justification?:\n \nA. Metaphysics\nB. Epistemology\nC. Aesthetics\nD. Ethics\n ",
        'answer': "B"
    },
    {
        'question': "What is the ethical philosophy that emphasizes the consequences of actions?:\n \nA. Deontology\nB. Virtue Ethics\nC. Utilitarianism\nD. Existentialism\n ",
        'answer': "C"
    },
    {
        'question': "Who is known as the 'Man of Steel'?:\n \nA. Batman\nB. Spider-Man\nC. Superman\nD. Iron Man\n ",
        'answer': "C"
    },
    {
        'question': "What is Batman's real name?:\n \nA. Bruce Wayne\nB. Clark Kent\nC. Tony Stark\nD. Peter Parker\n ",
        'answer': "A"
    },
    {
        'question': "Which superhero is also known as the 'God of Thunder'?:\n \nA. Thor\nB. Captain America\nC. Hulk\nD. Wolverine\n ",
        'answer': "A"
    },
    {
        'question': "Who is the alter ego of Spider-Man?:\n \nA. Bruce Banner\nB. Peter Parker\nC. Steve Rogers\nD. Logan\n ",
        'answer': "B"
    },
    {
        'question': "What is the name of Tony Stark's AI assistant in the Iron Man suit?:\n \nA. JARVIS\nB. HAL 9000\nC. Skynet\nD. C-3PO\n ",
        'answer': "A"
    },
    {
        'question': "Which superhero is known for wielding a shield made of vibranium?:\n \nA. Captain Marvel\nB. Black Panther\nC. Captain America\nD. Thor\n ",
        'answer': "C"
    },
    {
        'question': "What is the real name of the X-Men leader Professor X?:\n \nA. Erik Lehnsher\nB. Scott Summers\nC. Charles Xavier\nD. Jean Grey\n ",
        'answer': "C"
    },
    {
        'question': "Who is the arch-enemy of the Dark Knight, Batman?:\n \nA. Joker\nB. Riddler\nC. Two-Face\nD. Penguin\n ",
        'answer': "A"
    },
    {
        'question': "Which superhero is known for being the 'Merc with a Mouth'?:\n \nA. Wolverine\nB. Deadpool\nC. Iron Man\nD. Spider-Man\n ",
        'answer': "B"
    },
    {
        'question': "What is the name of the fictional city where most of the events in Batman comics take place?:\n \nA. Gotham City\nB. Metropolis\nC. Star City\nD. Central City\n ",
        'answer': "A"
    },
    {
        'question': "What is the national dish of the Philippines?:\n \nA. Sinigang\nB. Adobo\nC. Kare-Kare\nD. Lechon\n ",
        'answer': "B"
    },
    {
        'question': "Who is the national hero of the Philippines?:\n \nA. Andres Bonifacio\nB. Emilio Aguinaldo\nC. Jose Rizal\nD. Apolinario Mabini\n ",
        'answer': "C"
    },
    {
        'question': "What is the traditional Filipino dance often performed at celebrations and fiestas?:\n \nA. Tinikling\nB. Itik-Itik\nC. Singkil\nD. Pandanggo sa Ilaw\n ",
        'answer': "A"
    },
    {
        'question': "Which Filipino boxer is also known as 'Pac-Man'?:\n \nA. Manny Pacquiao\nB. Nonito Donaire\nC. Gerry Peñalosa\nD. Donnie Nietes\n ",
        'answer': "A"
    },
    {
        'question': "In what year did the Philippines gain independence from the United States?:\n \nA. 1898\nB. 1946\nC. 1965\nD. 1981\n ",
        'answer': "B"
    },
    {
        'question': "What is the traditional Filipino house called?:\n \nA. Bahay Kubo\nB. Nipa Hut\nC. Bahay na Bato\nD. Balay\n ",
        'answer': "A"
    },
    {
        'question': "Which Filipino dish is made with pork or chicken marinated in soy sauce, vinegar, garlic, and spices?:\n \nA. Adobo\nB. Sinigang\nC. Lechon\nD. Kare-Kare\n ",
        'answer': "A"
    },
    {
        'question': "What is the term for a Filipino mythological creature that is said to suck the blood of pregnant women?:\n \nA. Tikbalang\nB. Kapre\nC. Manananggal\nD. Duwende\n ",
        'answer': "C"
    },
    {
        'question': "Which Philippine island is known for its chocolate hills?:\n \nA. Bohol\nB. Palawan\nC. Mindoro\nD. Panay\n ",
        'answer': "A"
    },
    {
        'question': "What is the longest river in the Philippines?:\n \nA. Cagayan River\nB. Pasig River\nC. Agusan River\nD. Pampanga River\n ",
        'answer': "A"
    },
    {
        'question': "What is the SI unit of force?:\n \nA. Newton\nB. Joule\nC. Watt\nD. Pascal\n ",
        'answer': "A"
    },
    {
        'question': "Which law of motion states that an object at rest will remain at rest, and an object in motion will remain in motion with a constant velocity unless acted on by a net external force?:\n \nA. Newton's First Law\nB. Newton's Second Law\nC. Newton's Third Law\nD. Law of Inertia\n ",
        'answer': "A"
    },
    {
        'question': "What is the formula for calculating kinetic energy?:\n \nA. KE = mgh\nB. KE = 0.5 * mv^2\nC. KE = F * d\nD. KE = P/t\n ",
        'answer': "B"
    },
    {
        'question': "Which fundamental force is responsible for holding the nucleus of an atom together?:\n \nA. Gravity\nB. Electromagnetic Force\nC. Strong Nuclear Force\nD. Weak Nuclear Force\n ",
        'answer': "C"
    },
    {
        'question': "What is the speed of light in a vacuum?:\n \nA. 300,000 km/s\nB. 150,000 km/s\nC. 100,000 km/s\nD. 200,000 km/s\n ",
        'answer': "A"
    },
    {
        'question': "What is the law that states the total energy of an isolated system remains constant?:\n \nA. Law of Conservation of Energy\nB. Law of Conservation of Momentum\nC. Ohm's Law\nD. Boyle's Law\n ",
        'answer': "A"
    },
    {
        'question': "Which type of energy is associated with the motion of an object?:\n \nA. Potential Energy\nB. Kinetic Energy\nC. Mechanical Energy\nD. Thermal Energy\n ",
        'answer': "B"
    },
    {
        'question': "What is the unit of electrical resistance?:\n \nA. Ampere\nB. Ohm\nC. Volt\nD. Watt\n ",
        'answer': "B"
    },
    {
        'question': "According to Einstein's theory of relativity, what is the equivalent mass of an object as it approaches the speed of light?:\n \nA. Increases\nB. Decreases\nC. Remains the same\nD. Becomes zero\n ",
        'answer': "A"
    },
    {
        'question': "What is the formula for calculating gravitational force between two masses?:\n \nA. F = G * (m1 + m2)\nB. F = G * m1 * m2 / r^2\nC. F = m * a\nD. F = P / A\n ",
        'answer': "B"
    },
    {
        'question': "In the anime 'Naruto,' what is the name of Naruto Uzumaki's sensei?\n \nA. Kakashi Hatake\nB. Jiraiya\nC. Orochimaru\nD. Itachi Uchiha\n ",
        'answer': "A"
    },
    {
        'question': "Which anime follows the story of a young alchemist named Edward Elric and his brother Alphonse as they seek the Philosopher's Stone?\n \nA. Naruto\nB. Fullmetal Alchemist\nC. Attack on Titan\nD. Death Note\n ",
        'answer': "B"
    },
    {
        'question': "What is the name of the giant humanoid creatures that humanity must defend against in the anime 'Attack on Titan'?\n \nA. Titans\nB. Giants\nC. Colossi\nD. Mechs\n ",
        'answer': "A"
    },
    {
        'question': "In the anime 'One Piece,' what is the name of the main character who aims to become the Pirate King?\n \nA. Luffy\nB. Zoro\nC. Nami\nD. Sanji\n ",
        'answer': "A"
    },
    {
        'question': "What is the name of the notebook that allows its user to kill anyone by writing their name in it in the anime 'Death Note'?\n \nA. Soul Note\nB. Demon Diary\nC. Death Note\nD. Dark Journal\n ",
        'answer': "C"
    },
    {
        'question': "In the anime 'My Hero Academia,' what is the name of the main protagonist with the Quirk 'One For All'?\n \nA. Izuku Midoriya\nB. Katsuki Bakugo\nC. Shoto Todoroki\nD. All Might\n ",
        'answer': "A"
    },
    {
        'question': "Which anime follows the story of a young girl named Chihiro who becomes trapped in a mysterious and magical world?\n \nA. Spirited Away\nB. Howl's Moving Castle\nC. Princess Mononoke\nD. My Neighbor Totoro\n ",
        'answer': "A"
    },
    {
        'question': "In the anime 'Dragon Ball Z,' who is the prince of the Saiyan race?\n \nA. Goku\nB. Gohan\nC. Vegeta\nD. Piccolo\n ",
        'answer': "C"
    },
    {
        'question': "What is the name of the virtual reality MMORPG in the anime 'Sword Art Online'?\n \nA. Log Horizon\nB. Accel World\nC. ALfheim Online\nD. Aincrad\n ",
        'answer': "D"
    },
    {
        'question': "In the anime 'Demon Slayer: Kimetsu no Yaiba,' what is the main character Tanjiro Kamado's weapon of choice?\n \nA. Sword\nB. Bow\nC. Spear\nD. Axe\n ",
        'answer': "A"
    },
    {
        'question': "In the cartoon 'SpongeBob SquarePants,' what is the name of SpongeBob's best friend?\n \nA. Patrick Star\nB. Sandy Cheeks\nC. Squidward Tentacles\nD. Mr. Krabs\n ",
        'answer': "A"
    },
    {
        'question': "Which cartoon features a group of babies and their adventures, often led by a brave baby named Tommy Pickles?\n \nA. Rugrats\nB. The Powerpuff Girls\nC. Dexter's Laboratory\nD. Hey Arnold!\n ",
        'answer': "A"
    },
    {
        'question': "What is the name of the adventurous Monkey with a talking backpack in the cartoon 'Dora the Explorer'?\n \nA. Boots\nB. Swiper\nC. Tico\nD. Map\n ",
        'answer': "A"
    },
    {
        'question': "In the cartoon 'Tom and Jerry,' what type of animal is Jerry?\n \nA. Cat\nB. Mouse\nC. Dog\nD. Bird\n ",
        'answer': "B"
    },
    {
        'question': "Which cartoon features a boy with a magical, shape-shifting dog named Jake?\n \nA. Adventure Time\nB. The Fairly OddParents\nC. Ben 10\nD. Teen Titans Go!\n ",
        'answer': "A"
    },
    {
        'question': "What is the name of the clumsy and kind-hearted cat in the cartoon 'Garfield'?\n \nA. Odie\nB. Nermal\nC. Garfield\nD. Jon Arbuckle\n ",
        'answer': "C"
    },
    {
        'question': "In the cartoon 'Pokémon,' who is the main character that aspires to become a Pokémon Master?\n \nA. Misty\nB. Brock\nC. Ash Ketchum\nD. Jessie\n ",
        'answer': "C"
    },
    {
        'question': "What animated series features a group of kids with special abilities who come together to fight evil?\n \nA. Captain Planet and the Planeteers\nB. X-Men\nC. Teen Titans\nD. The Magic School Bus\n ",
        'answer': "C"
    },
    {
        'question': "In the cartoon 'The Flintstones,' what is the name of Fred Flintstone's best friend and next-door neighbor?\n \nA. Barney Rubble\nB. Wilma Flintstone\nC. Betty Rubble\nD. Dino\n ",
        'answer': "A"
    },
    {
        'question': "Which cartoon follows the adventures of a young boy and his Grandpa who travel through time and space?\n \nA. The Jetsons\nB. Time Squad\nC. Rick and Morty\nD. The Adventures of Jimmy Neutron: Boy Genius\n ",
        'answer': "C"
    },
    {
        'question': "What is the capital of France?\n \nA. Paris\nB. Rome\nC. Madrid\nD. Berlin\n",
        'answer': "A"
    },
    {
        'question': "Which city is the capital of Japan?\n \nA. Beijing\nB. Seoul\nC. Tokyo\nD. Bangkok\n",
        'answer': "C"
    },
    {
        'question': "What is the capital of Brazil?\n \nA. Buenos Aires\nB. Rio de Janeiro\nC. Brasília\nD. Santiago\n",
        'answer': "C"
    },
    {
        'question': "Which city serves as the capital of Australia?\n \nA. Wellington\nB. Canberra\nC. Sydney\nD. Melbourne\n",
        'answer': "B"
    },
    {
        'question': "What is the capital of Canada?\n \nA. Toronto\nB. Ottawa\nC. Vancouver\nD. Montreal\n",
        'answer': "B"
    },
    {
        'question': "Which city is the capital of Russia?\n \nA. St. Petersburg\nB. Moscow\nC. Kiev\nD. Warsaw\n",
        'answer': "B"
    },
    {
        'question': "What is the capital of South Africa?\n \nA. Cape Town\nB. Johannesburg\nC. Pretoria\nD. Durban\n",
        'answer': "C"
    },
    {
        'question': "Which city is the capital of China?\n \nA. Shanghai\nB. Beijing\nC. Hong Kong\nD. Taipei\n",
        'answer': "B"
    },
    {
        'question': "What is the capital of Mexico?\n \nA. Cancún\nB. Mexico City\nC. Guadalajara\nD. Monterrey\n",
        'answer': "B"
    },
    {
        'question': "Which city serves as the capital of Argentina?\n \nA. Buenos Aires\nB. Santiago\nC. Montevideo\nD. Lima\n",
        'answer': "A"
    },
    {
        'question': "What is the capital of India?\n \nA. New Delhi\nB. Mumbai\nC. Kolkata\nD. Chennai\n",
        'answer': "A"
    },
    {
        'question': "Which city is the capital of Germany?\n \nA. Frankfurt\nB. Munich\nC. Hamburg\nD. Berlin\n",
        'answer': "D"
    },
    {
        'question': "What is the capital of Egypt?\n \nA. Cairo\nB. Alexandria\nC. Luxor\nD. Giza\n",
        'answer': "A"
    },
    {
        'question': "Which city serves as the capital of the United Kingdom?\n \nA. London\nB. Manchester\nC. Birmingham\nD. Edinburgh\n",
        'answer': "A"
    },
    {
        'question': "What is the capital of Spain?\n \nA. Lisbon\nB. Barcelona\nC. Madrid\nD. Valencia\n",
        'answer': "C"
    },
    {
        'question': "Which city is the capital of Italy?\n \nA. Milan\nB. Rome\nC. Florence\nD. Venice\n",
        'answer': "B"
    },
    {
        'question': "What is the capital of South Korea?\n \nA. Seoul\nB. Busan\nC. Incheon\nD. Daegu\n",
        'answer': "A"
    },
    {
        'question': "Which city serves as the capital of Saudi Arabia?\n \nA. Riyadh\nB. Jeddah\nC. Mecca\nD. Medina\n",
        'answer': "A"
    },
    {
        'question': "What is the capital of Nigeria?\n \nA. Lagos\nB. Abuja\nC. Kano\nD. Ibadan\n",
        'answer': "B"
    },
    {
        'question': "Which city is the capital of Canada?\n \nA. Toronto\nB. Ottawa\nC. Vancouver\nD. Montreal\n",
        'answer': "B"
    },
    {
        'question': "Who is known as the 'King of Pop'?\n \nA. Prince\nB. Michael Jackson\nC. Madonna\nD. Elvis Presley\n",
        'answer': "B"
    },
    {
        'question': "Which Beatles album includes the song 'Hey Jude'?\n \nA. Abbey Road\nB. Rubber Soul\nC. The White Album\nD. Let It Be\n",
        'answer': "C"
    },
    {
        'question': "Who sang the theme song for the James Bond film 'Skyfall'?\n \nA. Adele\nB. Beyoncé\nC. Rihanna\nD. Lady Gaga\n",
        'answer': "A"
    },
    {
        'question': "Which rock band is known for the concept album 'The Wall'?\n \nA. Led Zeppelin\nB. The Rolling Stones\nC. Pink Floyd\nD. The Who\n",
        'answer': "C"
    },
    {
        'question': "What is the stage name of the lead singer of U2?\n \nA. Bono\nB. The Edge\nC. Adam Clayton\nD. Larry Mullen Jr.\n",
        'answer': "A"
    },
    {
        'question': "Which genre of music originated in Jamaica in the late 1960s?\n \nA. Reggae\nB. Salsa\nC. Jazz\nD. Blues\n",
        'answer': "A"
    },
    {
        'question': "Who won the 2019 Grammy Award for Album of the Year?\n \nA. Kendrick Lamar\nB. Taylor Swift\nC. Billie Eilish\nD. Adele\n",
        'answer': "C"
    },
    {
        'question': "Which female artist is known as the 'Queen of Soul'?\n \nA. Diana Ross\nB. Whitney Houston\nC. Aretha Franklin\nD. Beyoncé\n",
        'answer': "C"
    },
    {
        'question': "In which decade did Elvis Presley become widely known as the 'King of Rock and Roll'?\n \nA. 1950s\nB. 1960s\nC. 1970s\nD. 1980s\n",
        'answer': "A"
    },
    {
        'question': "Who is the lead vocalist of the band Queen?\n \nA. Roger Taylor\nB. Brian May\nC. John Deacon\nD. Freddie Mercury\n",
        'answer': "D"
    },
    {
        'question': "Which rapper released the album 'The Marshall Mathers LP'?\n \nA. Jay-Z\nB. Kanye West\nC. Eminem\nD. Drake\n",
        'answer': "C"
    },
    {
        'question': "What is the name of Beyoncé's fanbase?\n \nA. Beyhive\nB. Bey Nation\nC. Queen Bees\nD. Bey Lovers\n",
        'answer': "A"
    },
    {
        'question': "Who wrote the lyrics for the musical 'Les Misérables'?\n \nA. Andrew Lloyd Webber\nB. Stephen Sondheim\nC. Claude-Michel Schönberg\nD. Tim Rice\n",
        'answer': "C"
    },
    {
        'question': "Which country is known for the musical genre Flamenco?\n \nA. Brazil\nB. Spain\nC. Mexico\nD. Italy\n",
        'answer': "B"
    },
    {
        'question': "What is the best-selling album of all time?\n \nA. Thriller by Michael Jackson\nB. Back in Black by AC/DC\nC. The Dark Side of the Moon by Pink Floyd\nD. Rumours by Fleetwood Mac\n",
        'answer': "A"
    },
    {
        'question': "Which classical composer is known for his famous 'Moonlight Sonata'?\n \nA. Wolfgang Amadeus Mozart\nB. Ludwig van Beethoven\nC. Johann Sebastian Bach\nD. Franz Schubert\n",
        'answer': "B"
    },
    {
        'question': "Who sang 'Purple Haze' and is considered one of the greatest guitarists of all time?\n \nA. Jimi Hendrix\nB. Eric Clapton\nC. Jimmy Page\nD. Keith Richards\n",
        'answer': "A"
    },
    {
        'question': "Which famous opera features the aria 'Nessun Dorma'?\n \nA. Carmen\nB. La Traviata\nC. Turandot\nD. The Magic Flute\n",
        'answer': "C"
    },
    {
        'question': "What is the real name of the rapper Eminem?\n \nA. Marshall Mathers\nB. Curtis Jackson\nC. Calvin Broadus\nD. Shawn Carter\n",
        'answer': "A"
    },
    {
        'question': "Which rock band's members include Mick Jagger and Keith Richards?\n \nA. The Beatles\nB. The Rolling Stones\nC. Led Zeppelin\nD. The Who\n",
        'answer': "B"
    },
    {
        'question': "Who is known as the 'Material Girl'?\n \nA. Madonna\nB. Cher\nC. Lady Gaga\nD. Britney Spears\n",
        'answer': "A"
    },
    {
        'question': "What is the capital of Jazz?\n \nA. New Orleans\nB. Chicago\nC. New York\nD. Los Angeles\n",
        'answer': "A"
    },
    {
        'question': "Who was the lead singer of the band Nirvana?\n \nA. Dave Grohl\nB. Kurt Cobain\nC. Eddie Vedder\nD. Chris Cornell\n",
        'answer': "B"
    },
    {
        'question': "Which country is the birthplace of Tango music?\n \nA. Brazil\nB. Argentina\nC. Cuba\nD. Spain\n",
        'answer': "B"
    },
    {
        'question': "What is the name of Taylor Swift's first studio album?\n \nA. Fearless\nB. Speak Now\nC. Taylor Swift\nD. Red\n",
        'answer': "C"
    },
    {
        'question': "Who is known as the 'Godfather of Soul'?\n \nA. Marvin Gaye\nB. James Brown\nC. Otis Redding\nD. Sam Cooke\n",
        'answer': "B"
    },
    {
        'question': "Which instrument does Yo-Yo Ma play?\n \nA. Violin\nB. Cello\nC. Piano\nD. Trumpet\n",
        'answer': "B"
    },
    {
        'question': "What is the genre of music associated with Bob Marley?\n \nA. Reggae\nB. Hip Hop\nC. Jazz\nD. Blues\n",
        'answer': "A"
    },
    {
        'question': "Who is known as the 'King of OPM' (Original Pilipino Music)?\n \nA. Gary Valenciano\nB. Martin Nievera\nC. Rico J. Puno\nD. Jose Mari Chan\n",
        'answer': "A"
    },
    {
        'question': "What is the title of the song that made Freddie Aguilar internationally famous?\n \nA. Anak\nB. Bayan Ko\nC. Magtanim Ay Di Biro\nD. Kumusta Ka\n",
        'answer': "A"
    },
    {
        'question': "Who is known as the 'Queen of Philippine Movie and Music'?\n \nA. Lea Salonga\nB. Regine Velasquez\nC. Sharon Cuneta\nD. Nora Aunor\n",
        'answer': "D"
    },
    {
        'question': "Which Filipino band is famous for the hit songs '214' and 'Hinahanap-hanap Kita'?\n \nA. Eraserheads\nB. Parokya ni Edgar\nC. Rivermaya\nD. Bamboo\n",
        'answer': "C"
    },
    {
        'question': "What is the title of the song that catapulted Sarah Geronimo to fame?\n \nA. To Love You More\nB. Forever's Not Enough\nC. Tala\nD. Kilometro\n",
        'answer': "B"
    },
    {
        'question': "What band performed the song 'Kahit Ayaw Mo Na'?\n \nA. Slapshock\nB. This Band\nC. Ben&Ben\nD. Kamikazee\n",
        'answer': "B"
    },
    {
        'question': "Which Filipino singer is known for the song 'Harana'?\n \nA. Ogie Alcasid\nB. Parokya ni Edgar\nC. Eric Santos\nD. Parokya ni Leonil\n",
        'answer': "B"
    },
    {
        'question': "What is the title of the song by Yeng Constantino that became the theme song of the movie 'One More Try'?\n \nA. Salamat\nB. Ikaw\nC. Hawak Kamay\nD. Chinito\n",
        'answer': "B"
    },
    {
        'question': "Who is the lead vocalist of the band Itchyworms?\n \nA. Jugs Jugueta\nB. Jazz Nicolas\nC. Ely Buendia\nD. Chito Miranda\n",
        'answer': "B"
    },
    {
        'question': "What is the title of the novelty song popularized by Vhong Navarro?\n \nA. Totoy Bibo\nB. Otso Otso\nC. Boom Panes\nD. Pamela One\n",
        'answer': "A"
    },
    {
        'question': "Which Filipino rock band is known for the songs 'Alapaap' and 'With a Smile'?\n \nA. Eraserheads\nB. Parokya ni Edgar\nC. Rivermaya\nD. Sponge Cola\n",
        'answer': "A"
    },
    {
        'question': "Who is the 'Popstar Royalty' in the Philippines?\n \nA. Sarah Geronimo\nB. Regine Velasquez\nC. Lea Salonga\nD. Julie Anne San Jose\n",
        'answer': "A"
    },
    {
        'question': "Which Filipino singer is known for the song 'Himala'?\n \nA. Aegis\nB. Yano\nC. Rivermaya\nD. Asin\n",
        'answer': "C"
    },
    {
        'question': "What is the title of the song that became the first ever OPM song to reach 100 million views on YouTube?\n \nA. Buwan\nB. Kakaibabe\nC. Tala\nD. Mundo\n",
        'answer': "C"
    },
    {
        'question': "Who composed the song 'Awit ng Kabataan' performed by Rivermaya?\n \nA. Ely Buendia\nB. Rico Blanco\nC. Ryan Cayabyab\nD. Rey Valera\n",
        'answer': "B"
    },
    {
        'question': "Who is known as the 'Asia's Songbird'?\n \nA. Regine Velasquez\nB. Lani Misalucha\nC. Jaya\nD. Kuh Ledesma\n",
        'answer': "A"
    },
    {
        'question': "Which Filipino rock band is known for the song '214'?\n \nA. Parokya ni Edgar\nB. Rivermaya\nC. Eraserheads\nD. Silent Sanctuary\n",
        'answer': "B"
    },
    {
        'question': "What is the title of the song performed by Moira Dela Torre that became popular as a theme song for the movie 'The Hows of Us'?\n \nA. Tagpuan\nB. Torete\nC. Titibo-tibo\nD. Malaya\n",
        'answer': "A"
    },
    {
        'question': "What is the title of the song that became the official soundtrack of the movie 'One More Chance'?\n \nA. Ligaya\nB. Migraine\nC. It Might Be You\nD. Tuloy Pa Rin\n",
        'answer': "D"
    },
    {
        'question': "Who composed the song 'Himala' performed by Rivermaya?\n \nA. Ely Buendia\nB. Rico Blanco\nC. Rey Valera\nD. Ryan Cayabyab\n",
        'answer': "B"
    },
    {
        'question': "What is the title of the song by Shanti Dope that became popular for its catchy rap verses?\n \nA. Nadarang\nB. Amatz\nC. Hayaan Mo Sila\nD. Dalaga\n",
        'answer': "B"
    },
    {
        'question': "What does CPU stand for?\n \nA. Central Process Unit\nB. Central Processor Unit\nC. Computer Personal Unit\nD. Central Processing Unit\n",
        'answer': "D"
    },
    {
        'question': "Which programming language is often used for web development?\n \nA. Java\nB. Python\nC. HTML\nD. C++\n",
        'answer': "C"
    },
    {
        'question': "What is the purpose of RAM in a computer?\n \nA. Long-term storage\nB. Short-term memory\nC. Processing graphics\nD. Internet connection\n",
        'answer': "B"
    },
    {
        'question': "What does HTML stand for?\n \nA. Hyper Text Markup Language\nB. Hyperlinks and Text Markup Language\nC. Home Tool Markup Language\nD. Hyper Transfer Markup Language\n",
        'answer': "A"
    },
    {
        'question': "Which operating system is developed by Microsoft?\n \nA. Linux\nB. MacOS\nC. Windows\nD. Android\n",
        'answer': "C"
    },
    {
        'question': "What is the function of an operating system?\n \nA. Manage hardware resources\nB. Create documents\nC. Play music\nD. Edit images\n",
        'answer': "A"
    },
    {
        'question': "Which type of computer memory is non-volatile and can be electrically erased and reprogrammed?\n \nA. RAM\nB. ROM\nC. Cache Memory\nD. Flash Memory\n",
        'answer': "D"
    },
    {
        'question': "What does URL stand for?\n \nA. Uniform Resource Locator\nB. Universal Resource Locator\nC. Uniform Retrieval Locator\nD. Universal Retrieval Locator\n",
        'answer': "A"
    },
    {
        'question': "In computer programming, what does GUI stand for?\n \nA. General User Interface\nB. Graphical User Interface\nC. General Unifying Interface\nD. Graphical Unifying Interface\n",
        'answer': "B"
    },
    {
        'question': "Which company developed the Python programming language?\n \nA. Microsoft\nB. Apple\nC. Google\nD. Dropbox\n",
        'answer': "C"
    },
    {
        'question': "What is the purpose of a firewall in network security?\n \nA. Protect against viruses\nB. Monitor internet speed\nC. Block unauthorized access\nD. Encrypt data\n",
        'answer': "C"
    },
    {
        'question': "What does LAN stand for?\n \nA. Local Access Network\nB. Large Area Network\nC. Local Area Network\nD. Long-range Area Network\n",
        'answer': "C"
    },
    {
        'question': "Which programming language is commonly used for artificial intelligence?\n \nA. Java\nB. Python\nC. C#\nD. Ruby\n",
        'answer': "B"
    },
    {
        'question': "What is the primary purpose of an antivirus program?\n \nA. Speed up the computer\nB. Enhance graphics\nC. Protect against malware\nD. Improve internet connection\n",
        'answer': "C"
    },
    {
        'question': "What is the function of a router in a computer network?\n \nA. Connect devices within a local network\nB. Block internet access\nC. Manage printer settings\nD. Encrypt emails\n",
        'answer': "A"
    },
    {
        'question': "Which file format is commonly used for compressed archives?\n \nA. EXE\nB. ZIP\nC. MP3\nD. GIF\n",
        'answer': "B"
    },
    {
        'question': "What is the main purpose of an SSD (Solid State Drive) in a computer?\n \nA. Long-term storage\nB. Short-term memory\nC. Faster data access\nD. Optical disc reading\n",
        'answer': "C"
    },
    {
        'question': "Which programming language is often used for game development?\n \nA. Java\nB. Python\nC. C++\nD. HTML\n",
        'answer': "C"
    },
    {
        'question': "What does DNS stand for in the context of networking?\n \nA. Domain Name System\nB. Dynamic Network System\nC. Data Network Service\nD. Digital Naming Server\n",
        'answer': "A"
    },
    {
        'question': "Which of the following is a web browser?\n \nA. Microsoft Word\nB. Excel\nC. Firefox\nD. Photoshop\n",
        'answer': "C"
    },
    {
        'question': "What is the main function of an operating system?\n \nA. Run applications\nB. Manage hardware resources\nC. Create documents\nD. Play music\n",
        'answer': "B"
    },
    {
        'question': "Which programming language is commonly used for scientific and mathematical applications?\n \nA. Java\nB. Python\nC. MATLAB\nD. C#\n",
        'answer': "C"
    },
    {
        'question': "What does the acronym VPN stand for?\n \nA. Virtual Personal Network\nB. Very Private Network\nC. Virtual Private Network\nD. Visual Personal Network\n",
        'answer': "C"
    },
    {
        'question': "Which type of software provides additional functionalities to the operating system?\n \nA. Application Software\nB. System Software\nC. Utility Software\nD. Device Driver Software\n",
        'answer': "A"
    },
    {
        'question': "What is the purpose of a compiler in programming?\n \nA. Execute code\nB. Debug code\nC. Translate code to machine language\nD. Write code\n",
        'answer': "C"
    },
    {
        'question': "In computer networking, what does IP stand for?\n \nA. Internet Protocol\nB. Internal Protocol\nC. Internet Provider\nD. International Protocol\n",
        'answer': "A"
    },
    {
        'question': "What does SSD stand for in the context of data storage?\n \nA. Super Storage Drive\nB. Solid State Drive\nC. Software Storage Device\nD. System Storage Disk\n",
        'answer': "B"
    },
    {
        'question': "Which programming language is often used for developing mobile applications?\n \nA. Java\nB. Python\nC. Swift\nD. PHP\n",
        'answer': "C"
    },
    {
        'question': "What is the purpose of the 'Ctrl + Z' keyboard shortcut?\n \nA. Cut\nB. Copy\nC. Undo\nD. Redo\n",
        'answer': "C"
    },
    {
        'question': "Which component of a computer is responsible for managing and executing instructions?\n \nA. RAM\nB. CPU\nC. GPU\nD. Hard Drive\n",
        'answer': "B"
    },
    {
        'question': "Which company developed the Android operating system?\n \nA. Apple\nB. Samsung\nC. Google\nD. Microsoft\n",
        'answer': "C"
    },
    {
        'question': "What does GPS stand for in the context of smartphones?\n \nA. Global Programming System\nB. General Positioning System\nC. Geographic Positioning System\nD. Global Positioning System\n",
        'answer': "D"
    },
    {
        'question': "Which smartphone feature allows you to make payments using your device?\n \nA. NFC (Near Field Communication)\nB. Bluetooth\nC. Infrared\nD. Wi-Fi\n",
        'answer': "A"
    },
    {
        'question': "What is the name of Apple's virtual assistant on iOS devices?\n \nA. Alexa\nB. Siri\nC. Google Assistant\nD. Cortana\n",
        'answer': "B"
    },
    {
        'question': "Which smartphone manufacturer uses the slogan 'Never Settle'?\n \nA. Samsung\nB. Apple\nC. OnePlus\nD. Huawei\n",
        'answer': "C"
    },
    {
        'question': "What is the function of the 'Airplane Mode' on a smartphone?\n \nA. Enhance internet speed\nB. Save battery life\nC. Enable location tracking\nD. Boost processor performance\n",
        'answer': "B"
    },
    {
        'question': "Which smartphone brand is known for its 'Pixel' series?\n \nA. Samsung\nB. LG\nC. Google\nD. Sony\n",
        'answer': "C"
    },
    {
        'question': "What does IP67 certification mean for a smartphone?\n \nA. Water and dust resistance\nB. Enhanced processor speed\nC. Improved camera quality\nD. Longer battery life\n",
        'answer': "A"
    },
    {
        'question': "Which smartphone feature allows you to unlock your device using your fingerprint?\n \nA. Face ID\nB. Retina Scan\nC. Touch ID\nD. Iris Scan\n",
        'answer': "C"
    },
    {
        'question': "What is the name of Samsung's line of flagship smartphones?\n \nA. Xperia\nB. Galaxy\nC. Nexus\nD. Mate\n",
        'answer': "B"
    },
    {
        'question': "Which smartphone operating system is known for its open-source nature?\n \nA. iOS\nB. Android\nC. Windows Phone\nD. BlackBerry OS\n",
        'answer': "B"
    },
    {
        'question': "What is the purpose of a SIM card in a smartphone?\n \nA. Store contacts\nB. Expand storage\nC. Connect to the internet\nD. Identify the user to the network\n",
        'answer': "D"
    },
    {
        'question': "Which smartphone brand is associated with the 'Mate' and 'P' series?\n \nA. Apple\nB. Samsung\nC. Huawei\nD. LG\n",
        'answer': "C"
    },
    {
        'question': "What does OLED stand for in the context of smartphone displays?\n \nA. Organic Light Emitting Diode\nB. Overhead Light Emitting Display\nC. Optical Liquid Emitting Diode\nD. Outward Lighting Electronic Display\n",
        'answer': "A"
    },
    {
        'question': "Which smartphone feature allows you to wirelessly charge your device?\n \nA. NFC\nB. Bluetooth\nC. Infrared\nD. Qi Wireless Charging\n",
        'answer': "D"
    },
    {
        'question': "Which smartphone brand is known for its 'One' series?\n \nA. OnePlus\nB. Xiaomi\nC. Oppo\nD. Vivo\n",
        'answer': "A"
    },
    {
        'question': "What is the term for the small programs that add functionality to a smartphone?\n \nA. Widgets\nB. Apps\nC. Icons\nD. Shortcuts\n",
        'answer': "B"
    },
    {
        'question': "Which smartphone feature allows you to take 3D photos?\n \nA. Dual Cameras\nB. Augmented Reality\nC. Depth Sensor\nD. Slow-motion Capture\n",
        'answer': "C"
    },
    {
        'question': "Which smartphone brand is known for its 'Redmi' and 'Mi' series?\n \nA. Oppo\nB. Xiaomi\nC. Vivo\nD. Realme\n",
        'answer': "B"
    },
    {
        'question': "What is the purpose of the 'Do Not Disturb' mode on a smartphone?\n \nA. Increase screen brightness\nB. Block unwanted calls and notifications\nC. Enhance speaker volume\nD. Enable voice command recognition\n",
        'answer': "B"
    },
    {
        'question': "Which smartphone brand is associated with the 'Xperia' series?\n \nA. Sony\nB. Nokia\nC. Motorola\nD. HTC\n",
        'answer': "A"
    },
    {
        'question': "What does AMOLED stand for in the context of smartphone displays?\n \nA. Advanced Mobile Organic Light Emitting Diode\nB. Active Matrix Organic Light Emitting Diode\nC. Amorphous Mobile Organic Light Emitting Diode\nD. Adaptive Mobile Organic Light Emitting Diode\n",
        'answer': "B"
    },
    {
        'question': "Which smartphone feature allows you to control the device by moving your eyes?\n \nA. Eye ID\nB. Gaze Recognition\nC. Blink Control\nD. Eye Tracking\n",
        'answer': "D"
    },
    {
        'question': "What is the term for the technology that allows a smartphone screen to recognize different levels of pressure?\n \nA. Force Touch\nB. Multi-Touch\nC. Haptic Feedback\nD. Gesture Control\n",
        'answer': "A"
    },
    {
        'question': "In which city is Phinma Cagayan de Oro College located?\n \nA. Manila\nB. Cebu\nC. Davao\nD. Cagayan de Oro\n",
        'answer': "D"
    },
    {
        'question': "What is the official name of the college?\n \nA. Phinma University\nB. Cagayan de Oro College\nC. Mindanao College\nD. Phinma Cagayan de Oro College\n",
        'answer': "D"
    },
    {
        'question': "Which year was Phinma Cagayan de Oro College established?\n \nA. 1970\nB. 1985\nC. 1999\nD. 2005\n",
        'answer': "B"
    },
    {
        'question': "What is the official mascot of Phinma Cagayan de Oro College?\n \nA. Eagles\nB. Tigers\nC. Panthers\nD. Bulldogs\n",
        'answer': "A"
    },
    {
        'question': "What is the college's official color?\n \nA. Blue and White\nB. Red and Gold\nC. Green and Yellow\nD. Maroon and White\n",
        'answer': "C"
    },
    {
        'question': "Which sports are commonly played or supported at Phinma Cagayan de Oro College?\n \nA. Basketball\nB. Volleyball\nC. Soccer\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "How many campuses does Phinma Cagayan de Oro College have?\n \nA. One\nB. Two\nC. Three\nD. Four\n",
        'answer': "A"
    },
    {
        'question': "What is the college's vision and mission statement?\n \nA. To provide quality education for all\nB. To be a leading institution in the region\nC. To promote excellence in research\nD. Please specify\n",
        'answer': "D"
    },
    {
        'question': "Which accreditation bodies recognize Phinma Cagayan de Oro College?\n \nA. CHED\nB. PACUCOA\nC. TESDA\nD. Both A and B\n",
        'answer': "D"
    },
    {
        'question': "What is the college's commitment to community service or social responsibility?\n \nA. Outreach programs\nB. Scholarship opportunities\nC. Environmental initiatives\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "What facilities or amenities does Phinma Cagayan de Oro College offer to students?\n \nA. Modern classrooms\nB. Sports facilities\nC. Libraries\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "Which student organizations are active at Phinma Cagayan de Oro College?\n \nA. Student Council\nB. Honor Society\nC. Cultural Clubs\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "How does Phinma Cagayan de Oro College support student development and success?\n \nA. Academic advising\nB. Career counseling\nC. Leadership programs\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "What initiatives or programs does the college have to promote diversity and inclusivity?\n \nA. Cultural events\nB. Gender sensitivity programs\nC. Special education courses\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "Which scholarships or financial aid programs are available for students at Phinma Cagayan de Oro College?\n \nA. Merit-based scholarships\nB. Need-based scholarships\nC. Sports scholarships\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "What are the key strengths or distinguishing features of Phinma Cagayan de Oro College?\n \nA. Academic excellence\nB. Strong faculty\nC. Industry partnerships\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "How does the college engage with the local community or industry?\n \nA. Internship programs\nB. Industry advisory boards\nC. Community outreach\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "What is the college's stance on environmental sustainability?\n \nA. Green initiatives\nB. Recycling programs\nC. Energy conservation\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "How does Phinma Cagayan de Oro College prepare students for the workforce?\n \nA. Career development services\nB. Industry-relevant curriculum\nC. Internship opportunities\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "Which technology or e-learning platforms does Phinma Cagayan de Oro College use for online education?\n \nA. Moodle\nB. Google Classroom\nC. Blackboard\nD. All of the above\n",
        'answer': "D"
    },
    {
        'question': "In which Philippine region is Cagayan de Oro City located?\n \nA. Luzon\nB. Visayas\nC. Mindanao\nD. National Capital Region\n",
        'answer': "C"
    },
    {
        'question': "What is the nickname of Cagayan de Oro City?\n \nA. City of Smiles\nB. Gateway to Northern Mindanao\nC. Queen City of the South\nD. Pearl of the Orient\n",
        'answer': "B"
    },
    {
        'question': "Which river runs through Cagayan de Oro City?\n \nA. Agusan River\nB. Cagayan River\nC. Chico River\nD. Pulangi River\n",
        'answer': "B"
    },
    {
        'question': "What is the meaning of 'Cagayan de Oro' in Spanish?\n \nA. River of Gold\nB. City of Friendship\nC. Golden City\nD. Land of Promise\n",
        'answer': "A"
    },
    {
        'question': "Cagayan de Oro is known for its annual festival called?\n \nA. Panagbenga Festival\nB. Kadayawan Festival\nC. Higalaay Festival\nD. Sinulog Festival\n",
        'answer': "C"
    },
    {
        'question': "What prominent landmark in Cagayan de Oro City is known for its historical significance?\n \nA. St. Augustine Metropolitan Cathedral\nB. Divine Mercy Shrine\nC. Plaza Divisoria\nD. MacArthur Marker\n",
        'answer': "D"
    },
    {
        'question': "Which of the following industries is a major contributor to Cagayan de Oro City's economy?\nA. Tourism\nB. Manufacturing\nC. Agriculture\nD. Mining\n",
        'answer': "B"
    },
    {
        'question': "Cagayan de Oro is often referred to as the 'City of Golden ______.'\n \nA. Friendship\nB. Opportunities\nC. Harvest\nD. Friendship\n",
        'answer': "D"
    },
    {
        'question': "Which mountain range is near Cagayan de Oro City?\n \nA. Sierra Madre\nB. Zambales Mountains\nC. Kitanglad Mountain Range\nD. Caraballo Mountains\n",
        'answer': "C"
    },
    {
        'question': "What is the name of the famous water rafting river in Cagayan de Oro City?\n \nA. Agus River\nB. Chico River\nC. Cagayan River\nD. Agusan River\n",
        'answer': "C"
    },
    {
        'question': "Which government district is located in the heart of Cagayan de Oro City?\n \nA. Malasag\nB. Carmen\nC. Divisoria\nD. Macabalan\n",
        'answer': "C"
    },
    {
        'question': "What is the main mode of transportation within Cagayan de Oro City?\n \nA. Jeepneys\nB. Tricycles\nC. Taxis\nD. Motorcycles\n",
        'answer': "A"
    },
    {
        'question': "What is the name of the seaport in Cagayan de Oro City?\n \nA. Cagayan de Oro Port\nB. Macabalan Port\nC. Puerto de Oro\nD. Cagayan Port\n",
        'answer': "B"
    },
    {
        'question': "Which of the following universities is located in Cagayan de Oro City?\n \nA. Ateneo de Davao University\nB. Xavier University - Ateneo de Cagayan\nC. Mindanao State University\nD. University of the Philippines Cebu\n",
        'answer': "B"
    },
    {
        'question': "Cagayan de Oro is known for its white-water rafting adventure. Which river is famous for this activity\n ?\nA. Chico River\nB. Cagayan River\nC. Agus River\nD. Pulangi River\n",
        'answer': "B"
    },
    {
        'question': "Which famous park in Cagayan de Oro City offers panoramic views of the city?\n \nA. Gaston Park\nB. Gardens of Malasag Eco-Tourism Village\nC. Rodelsa Circle\nD. Mapawa Nature Park\n",
        'answer': "B"
    },
    {
        'question': "What is the meaning of 'Higalaay,' the festival celebrated in Cagayan de Oro City?\n \nA. Celebration\nB. Unity\nC. Friendship\nD. Happiness\n",
        'answer': "C"
    },
    {
        'question': "What is the name of the popular public market in Cagayan de Oro City?\n \nA. Divisoria Market\nB. Carmen Market\nC. Agora Market\nD. Ororama Supercenter\n",
        'answer': "C"
    },
    {
        'question': "Which government building is located at the center of Divisoria in Cagayan de Oro City?\n \nA. City Hall\nB. Provincial Capitol\nC. City Library\nD. Regional Trial Court\n",
        'answer': "A"
    },
    {
        'question': "What is the name of the historical bridge in Cagayan de Oro City that connects the Lapasan and Macabalan sides of the city?\n \nA. Marcos Bridge\nB. MacArthur Bridge\nC. Kagay-an Bridge\nD. Jones Bridge\n",
        'answer': "C"
    },
    {
        'question': "Who is known as the 'Queen of All Media' in the Philippines?\n \nA. Kathryn Bernardo\nB. Anne Curtis\nC. Kris Aquino\nD. Angel Locsin\n",
        'answer': "C"
    },
    {
        'question': "Which Filipino actor is also a popular host of the reality show 'Pinoy Big Brother'?\n \nA. Coco Martin\nB. Vice Ganda\nC. Boy Abunda\nD. Daniel Padilla\n",
        'answer': "C"
    },
    {
        'question': "Who played the lead role in the TV series 'Darna' in 2005?\n \nA. Angel Locsin\nB. Marian Rivera\nC. Jennylyn Mercado\nD. Nadine Lustre\n",
        'answer': "A"
    },
    {
        'question': "In the TV series 'Forevermore,' who played the role of Xander?\n \nA. James Reid\nB. Enrique Gil\nC. Alden Richards\nD. Jericho Rosales\n",
        'answer': "B"
    },
    {
        'question': "Which actress is known for her role as Maya in the TV series 'Be Careful with My Heart'?\n \nA. Jodi Sta. Maria\nB. Kim Chiu\nC. Maja Salvador\nD. Erich Gonzales\n",
        'answer': "A"
    },
    {
        'question': "Who is the lead actor in the TV series 'Ang Probinsyano'?\n \nA. Coco Martin\nB. Dingdong Dantes\nC. Gerald Anderson\nD. John Lloyd Cruz\n",
        'answer': "A"
    },
    {
        'question': "In the reality show 'It's Showtime,' who is known for the catchphrase 'Sample, Sample'?\n \nA. Vice Ganda\nB. Jhong Hilario\nC. Anne Curtis\nD. Vhong Navarro\n",
        'answer': "B"
    },
    {
        'question': "Which Kapamilya actress gained fame for her role as 'Yaya Dub' in the noontime show 'Eat Bulaga!'?\n \nA. Maine Mendoza\nB. Julia Montes\nC. Liza Soberano\nD. Angelica Panganiban\n",
        'answer': "A"
    },
    {
        'question': "Who is the lead actress in the TV series 'Wildflower'?\n \nA. Maja Salvador\nB. Julia Montes\nC. Angel Locsin\nD. Sunshine Cruz\n",
        'answer': "A"
    },
    {
        'question': "In the teleserye 'Pangako Sa 'Yo,' who portrayed the character of Angelo Buenavista?\n \nA. Daniel Padilla\nB. Jericho Rosales\nC. Piolo Pascual\nD. John Lloyd Cruz\n",
        'answer': "B"
    },
    {
        'question': "Which celebrity hosts the talk show 'Tonight with Boy Abunda'?\n \nA. Boy Abunda\nB. Kris Aquino\nC. Vice Ganda\nD. Toni Gonzaga\n",
        'answer': "A"
    },
    {
        'question': "Who played the iconic role of 'Mang Kepweng' in a comedy fantasy series?\n \nA. Jose Manalo\nB. Michael V.\nC. Vic Sotto\nD. Wally Bayola\n",
        'answer': "B"
    },
    {
        'question': "In the TV series 'Got to Believe,' who starred alongside Daniel Padilla?\n \nA. Kathryn Bernardo\nB. Liza Soberano\nC. Nadine Lustre\nD. Julia Montes\n",
        'answer': "A"
    },
    {
        'question': "Who is known as the 'Dancing Queen' and 'Dance Diva' in the Philippines?\n \nA. Regine Velasquez\nB. Sarah Geronimo\nC. Anne Curtis\nD. Toni Gonzaga\n",
        'answer': "C"
    },
    {
        'question': "Which celebrity is often referred to as the 'Asia's Songbird'?\n \nA. Sarah Geronimo\nB. Regine Velasquez\nC. Lea Salonga\nD. Jaya\n",
        'answer': "B"
    },
    {
        'question': "In the TV series 'Ika-5 Utos,' who portrayed the character of Clarisse?\n \nA. Sunshine Cruz\nB. Ina Raymundo\nC. Jean Garcia\nD. Alice Dixson\n",
        'answer': "A"
    },
    {
        'question': "Who is the lead actor in the TV series 'The General's Daughter'?\n \nA. Dingdong Dantes\nB. Gerald Anderson\nC. Jericho Rosales\nD. Coco Martin\n",
        'answer': "B"
    },
    {
        'question': "Which actor is known for his portrayal of 'Cardo Dalisay' in 'Ang Probinsyano'?\n \nA. John Lloyd Cruz\nB. Alden Richards\nC. Coco Martin\nD. Jericho Rosales\n",
        'answer': "C"
    },
    {
        'question': "Who is the host of the popular game show 'Wowowin'?\n \nA. Willie Revillame\nB. Vice Ganda\nC. Ryan Bang\nD. Vhong Navarro\n",
        'answer': "A"
    },
    {
        'question': "In the TV series 'The Killer Bride,' who played the role of Emma Bonaobra?\n \nA. Janella Salvador\nB. Maja Salvador\nC. Julia Montes\nD. Angel Locsin\n",
        'answer': "A"
    },
    {
        'question': "What is the chemical symbol for gold?\n \nA. Gd\nB. Au\nC. Ag\nD. Fe\n",
        'answer': "B"
    },
    {
        'question': "Which gas is essential for respiration?\n \nA. Oxygen\nB. Carbon Dioxide\nC. Nitrogen\nD. Hydrogen\n",
        'answer': "A"
    },
    {
        'question': "What is the pH value of a neutral substance?\n \nA. 7\nB. 0\nC. 14\nD. 1\n",
        'answer': "A"
    },
    {
        'question': "Which element has the chemical symbol 'O'?\n \nA. Oxygen\nB. Osmium\nC. Octane\nD. Ozone\n",
        'answer': "A"
    },
    {
        'question': "What is the chemical formula for water?\n \nA. H2O2\nB. CO2\nC. H2O\nD. CH4\n",
        'answer': "C"
    },
    {
        'question': "Which gas do plants absorb during photosynthesis?\n \nA. Oxygen\nB. Nitrogen\nC. Carbon Dioxide\nD. Hydrogen\n",
        'answer': "C"
    },
    {
        'question': "What is the chemical symbol for iron?\n \nA. Fe\nB. Ir\nC. In\nD. Au\n",
        'answer': "A"
    },
    {
        'question': "Which element is essential for human bone health?\n \nA. Magnesium\nB. Calcium\nC. Potassium\nD. Sodium\n",
        'answer': "B"
    },
    {
        'question': "What is the chemical symbol for sodium?\n \nA. So\nB. Sn\nC. Na\nD. Ni\n",
        'answer': "C"
    },
    {
        'question': "What is the process of a substance changing from a gas to a liquid?\n \nA. Condensation\nB. Sublimation\nC. Evaporation\nD. Melting\n",
        'answer': "A"
    },
    {
        'question': "Which gas makes up the majority of Earth's atmosphere?\n \nA. Oxygen\nB. Carbon Dioxide\nC. Nitrogen\nD. Hydrogen\n",
        'answer': "C"
    },
    {
        'question': "What is the chemical symbol for helium?\n \nA. H\nB. He\nC. Be\nD. Ne\n",
        'answer': "B"
    },
    {
        'question': "What is the chemical formula for methane?\n \nA. CH3OH\nB. C6H12O6\nC. CH4\nD. CO2\n",
        'answer': "C"
    },
    {
        'question': "Which subatomic particle carries a positive charge?\n \nA. Proton\nB. Neutron\nC. Electron\nD. Photon\n",
        'answer': "A"
    },
    {
        'question': "What is the chemical symbol for carbon?\n \nA. Co\nB. Cr\nC. Ca\nD. C\n",
        'answer': "D"
    },
    {
        'question': "What is the process of a substance changing from a liquid to a gas?\n \nA. Condensation\nB. Sublimation\nC. Evaporation\nD. Melting\n",
        'answer': "C"
    },
    {
        'question': "Which element is a noble gas?\n \nA. Neon\nB. Sodium\nC. Nickel\nD. Nitrogen\n",
        'answer': "A"
    },
    {
        'question': "What is the chemical symbol for silver?\n \nA. Si\nB. Sr\nC. Sn\nD. Ag\n",
        'answer': "D"
    },
    {
        'question': "What is the chemical formula for table salt?\n \nA. NaCl\nB. HCl\nC. KCl\nD. CaCl2\n",
        'answer': "A"
    },
    {
        'question': "Which gas is responsible for the greenhouse effect?\n \nA. Oxygen\nB. Nitrogen\nC. Carbon Dioxide\nD. Helium\n",
        'answer': "C"
    },
    {
        'question': "What is the name of the document that formally proclaimed the independence of the Philippines from Spanish colonization?\n \nA. Pact of Biak-na-Bato\nB. Treaty of Paris\nC. Malolos Constitution\nD. Declaration of Independence\n",
        'answer': "C"
    },
    {
        'question': "During which war did the Philippines gain independence from the United States?\n \nA. World War I\nB. World War II\nC. Philippine-American War\nD. Vietnam War\n",
        'answer': "B"
    },
    {
        'question': "What was the name of the secret society founded by Andres Bonifacio that aimed to overthrow Spanish rule?\n \nA. Katipunan\nB. KKK\nC. Liga Filipina\nD. La Solidaridad\n",
        'answer': "A"
    },
    {
        'question': "Who led the famous Cry of Pugad Lawin that marked the beginning of the Philippine Revolution against Spanish rule?\n \nA. Jose Rizal\nB. Andres Bonifacio\nC. Emilio Aguinaldo\nD. Apolinario Mabini\n",
        'answer': "B"
    },
    {
        'question': "What event marked the end of Japanese occupation in the Philippines during World War II?\n \nA. Battle of Manila\nB. Liberation of Manila\nC. Battle of Bataan\nD. Leyte Landing\n",
        'answer': "B"
    },
    {
        'question': "Who was the leader of the Philippine revolution against Spanish colonization?\n \nA. Jose Rizal\nB. Andres Bonifacio\nC. Emilio Aguinaldo\nD. Antonio Luna\n",
        'answer': "B"
    },
    {
        'question': "In what year did the Philippines officially become a republic?\n \nA. 1898\nB. 1901\nC. 1946\nD. 1965\n",
        'answer': "C"
    },
    {
        'question': "What is the longest-running constitution in Philippine history?\n \nA. 1935 Constitution\nB. 1943 Constitution\nC. 1973 Constitution\nD. 1987 Constitution\n",
        'answer': "D"
    },
    {
        'question': "Who was the leader of the Katipunan who became the first President of the Philippines?\n \nA. Emilio Aguinaldo\nB. Andres Bonifacio\nC. Antonio Luna\nD. Apolinario Mabini\n",
        'answer': "A"
    },
    {
        'question': "Who was the first Filipino to circumnavigate the globe?\n \nA. Lapu-Lapu\nB. Ferdinand Magellan\nC. Jose Rizal\nD. Antonio Pigafetta\n",
        'answer': "D"
    },
    {
        'question': "What is the name of the document that ended the hostilities between the Philippines and the United States in 1946?\n \nA. Treaty of Paris\nB. Tydings-McDuffie Act\nC. Laurel-Langley Agreement\nD. Bell Trade Act\n",
        'answer': "B"
    },
    {
        'question': "Which event is known as the EDSA Revolution that led to the ousting of President Ferdinand Marcos?\n \nA. EDSA I\nB. EDSA II\nC. EDSA III\nD. People Power Revolution\n",
        'answer': "A"
    },
    {
        'question': "Who was the first woman to become President of the Philippines?\n \nA. Gloria Macapagal-Arroyo\nB. Corazon Aquino\nC. Imelda Marcos\nD. Miriam Defensor-Santiago\n",
        'answer': "B"
    },
    {
        'question': "During which historical event did Lapu-Lapu defeat Ferdinand Magellan?\n \nA. Battle of Mactan\nB. Battle of Manila Bay\nC. Battle of Bataan\nD. Battle of Pulo Aura\n",
        'answer': "A"
    },
    {
        'question': "What is the term used to refer to the period of Spanish colonization in the Philippines?\n \nA. Renaissance\nB. Exploration Age\nC. Colonial Era\nD. Spanish Regime\n",
        'answer': "D"
    },
    {
        'question': "Which Philippine hero is known for his role in the Propaganda Movement and his writings such as 'Noli Me Tangere' and 'El Filibusterismo'?\n \nA. Jose Rizal\nB. Andres Bonifacio\nC. Emilio Aguinaldo\nD. Marcelo H. del Pilar\n",
        'answer': "A"
    },
    {
        'question': "What is the largest city in Mindanao?\n \nA. Davao City\nB. Cagayan de Oro City\nC. General Santos City\nD. Zamboanga City\n",
        'answer': "A"
    },
    {
        'question': "Which mountain is the highest peak in Mindanao?\n \nA. Mount Apo\nB. Mount Kitanglad\nC. Mount Matutum\nD. Mount Malindang\n",
        'answer': "A"
    },
    {
        'question': "Which lake is the largest in Mindanao?\n \nA. Lake Mainit\nB. Lake Sebu\nC. Lake Lanao\nD. Lake Holon\n",
        'answer': "C"
    },
    {
        'question': "Which river is the longest in Mindanao?\n \nA. Rio Grande de Mindanao\nB. Mindanao River\nC. Pulangi River\nD. Tagoloan River\n",
        'answer': "A"
    },
    {
        'question': "In which province can you find the Enchanted River, known for its clear blue waters and mysterious depths?\n \nA. Surigao del Norte\nB. Surigao del Sur\nC. Agusan del Norte\nD. Agusan del Sur\n",
        'answer': "B"
    },
    {
        'question': "Which province is known as the 'Durian Capital of the Philippines'?\n \nA. Bukidnon\nB. Cagayan de Oro City\nC. Wao City\nD. Davao\n",
        'answer': "D"
    },
    {
        'question': "In which region is the Zamboanga Peninsula located?\n \nA. Northern Mindanao\nB. Davao Region\nC. Soccsksargen\nD. Zamboanga Peninsula\n",
        'answer': "D"
    },
    {
        'question': "What is the southernmost province in Mindanao?\n \nA. Davao del Sur\nB. Sarangani\nC. South Cotabato\nD. Tawi-Tawi\n",
        'answer': "D"
    },
    {
        'question': "Which mountain range runs through the eastern part of Mindanao?\n \nA. Sierra Madre\nB. Cordillera Central\nC. Zambales Mountains\nD. Diwata Mountains\n",
        'answer': "D"
    },
    {
        'question': "Which lake in Mindanao is known for its floating village and tilapia aquaculture?\n \nA. Lake Mainit\nB. Lake Sebu\nC. Lake Lanao\nD. Lake Holon\n",
        'answer': "B"
    },
    {
        'question': "In which province can you find the Maria Cristina Falls, often called the 'Mother of Industry'?\n \nA. Lanao del Norte\nB. Bukidnon\nC. Misamis Occidental\nD. Zamboanga del Sur\n",
        'answer': "A"
    },
    {
        'question': "Which city is known as the 'City of Golden Friendship' in Mindanao?\n \nA. Cagayan de Oro City\nB. Davao City\nC. General Santos City\nD. Iligan City\n",
        'answer': "A"
    },
    {
        'question': "What is the name of the famous white-sand beach in Surigao del Norte known for its clear blue waters?\n \nA. Dahican Beach\nB. Britania Islands\nC. Siargao Island\nD. Bucas Grande Island\n",
        'answer': "C"
    },
    {
        'question': "Which city is the largest in terms of land area in Mindanao?\n \nA. Davao City\nB. Cagayan de Oro City\nC. General Santos City\nD. Zamboanga City\n",
        'answer': "A"
    },
    {
        'question': "Which mountain range extends through the Zamboanga Peninsula in Mindanao?\n \nA. Zambales Cordilleras\nB. Diwata Mountains\nC. Caraballo Mountains\nD. Cordillera Central\n",
        'answer': "A"
    },
    {
        'question': "In which province can you find the scenic Asik-Asik Falls, known for its curtain-like appearance?\n \nA. Cotabato\nB. Sultan Kudarat\nC. Maguindanao\nD. North Cotabato\n",
        'answer': "D"
    },
    {
        'question': "Which region is known for its vast pineapple plantations and is often called the 'Fruit Basket of the Philippines'?\n \nA. Bukidnon\nB. Northern Mindanao\nC. Soccsksargen\nD. Zamboanga Peninsula\n",
        'answer': "A"
    },
]

names = []

total_timer = []

score = []

remarks = []

while game_running:
    random.shuffle(questions)
    player_score = 0
    score_limit = 100
    fail_limit = -abs(100)
    print("MIND MASTERS\nv1.0.0beta\n")
    print("Main Menu")
    print()
    print("1. Start Game")
    print("2. Instructions")
    print("3. Leaderboard")
    print("4. Exit")
    print()
    player_option = int(input("Please Select an Option (1, 2, 3, 4): "))
    print()
    if player_option == 1:
        player_name = input("Enter Your Name: ")
        names.append(player_name)
        print()
        print("--------------------------------------------")
        print("               LOADING GAME                 ")
        print("                PLEASE WAIT                 ")
        print("--------------------------------------------")
        print()
        time.sleep(2)
        print("--------------------------------------------")
        print("                  START!                    ")
        print("--------------------------------------------")
        print()
        time.sleep(1)
        start_timer = time.time()
        for question in questions:
            question_text = question.get("question")
            print(question_text)
            print()
            user_answer = input("Enter (A, B, C, D): ").upper()
            if user_answer not in ['A', 'B', 'C', 'D']:
                print("Invalid input. Please enter A, B, C, or D.")
            print()
            correct_answer = question.get("answer")
            if user_answer == correct_answer:
                print("Your answer is correct!")
                player_score += 15
                print(player_name + ", your Score is:", player_score)
                print()
                print("--------------------------------------------")
                print()
            else:
                print(user_answer,"is Incorrect!")
                print("The correct answer is,", correct_answer)
                player_score -= 25
                print(player_name +", your Score is:", player_score)
                print()
                print("--------------------------------------------")
                print()
            time.sleep(1)
            total_time = time.time() - start_timer
            if player_score <= fail_limit:
                time.sleep(1)
                print("--------------------------------------------------------------------------------------------------")
                print("--------------------------------------------------------------------------------------------------")
                print("                                        YOU FAILED!                                               ")
                print("                                         GAME OVER                                                ")
                print("                                    BETTER LUCK NEXT TIME!                                        ")
                print("                                     Your score is,",player_score                                  )
                print("--------------------------------------------------------------------------------------------------")
                print("--------------------------------------------------------------------------------------------------")
                fail_remarks = "| FAILED"
                remarks.append(fail_remarks)
                score.append(player_score)
                total_timer.append(int(total_time))
                print()
                break
            elif player_score >= score_limit:
                time.sleep(1)
                print("--------------------------------------------------------------------------------------------------")              
                print("--------------------------------------------------------------------------------------------------")
                print("                                         GREAT!                                                   ")
                print("                                        YOU WIN!                                                  ")
                print("                        You have reached 100 points in",int(total_time),"seconds                 ")
                print("                                    TOTAL: SCORE:",player_score                                    )
                print("--------------------------------------------------------------------------------------------------")
                print("--------------------------------------------------------------------------------------------------")
                passed_remarks = "| PASSED"
                remarks.append(passed_remarks)
                score.append(player_score)
                total_timer.append(int(total_time))
                time.sleep(1)
                print()   
                print("                  Congratulations,",player_name,". You are a certified Mind Master                    ")
                time.sleep(1)                
                print()
                print()
                break
    elif player_option == 2:
        time.sleep(2)
        print("--------------------------------------------------------------------------------------------------")
        print("                                    GAME INSTRUCTIONS                                             ")
        print("--------------------------------------------------------------------------------------------------")
        time.sleep(1)
        print()
        print("The quizz consists of questions carefully designed to help you self-assess your general knowledge.")
        time.sleep(1)
        print("Each question in the quiz is of multiple-choice format. Read each question carefully.")
        time.sleep(1)
        print("Answer each question by typing the LETTER of your chosen answer.")
        time.sleep(1)
        print("Each CORRECT ANSWER will INCREASE your score by 15 POINTS.")
        time.sleep(1)
        print("If you reach 100 POINTS the quiz will END!")
        time.sleep(1)
        print("But for every WRONG ANSWER, your score will be DEDUCTED by 25 POINTS.")
        time.sleep(1)
        print("It is GAME OVER if your score reaches -100 points.")
        time.sleep(1)
        print("The quiz tracks your TIME to reach 100 POINTS")
        time.sleep(1)
        print("The Player who will reach 100 POINTS the FASTEST is the TRUE MIND MASTER!")
        time.sleep(1)
        print("Good Luck and Enjoy!")
        time.sleep(1)
        print()
        print("-DEVS")
        time.sleep(1)
        print()
        print("--------------------------------------------------------------------------------------------------")
        print("                                 MIND MASTERS v1.0.0beta                                          ")
        print("--------------------------------------------------------------------------------------------------")
        print()
        print()
    elif player_option == 3:
        time.sleep(2)
        if total_timer == [] and names == [] and score == []:
            print("--------------------------------------------------------------------------------------------------")
            print("                                      LEADERBOARD                                                 ")
            print("--------------------------------------------------------------------------------------------------")
            print()
            print("                      PLEASE PLAY THE GAME TO POPULATE THE LEADERBOARD                            ")
            print()
            print("--------------------------------------------------------------------------------------------------")
            print("                                MIND MASTERS v1.0.0beta                                           ")
            print("--------------------------------------------------------------------------------------------------")
            print()
        else:
            print("--------------------------------------------------------------------------------------------------")
            print("                                      LEADERBOARD                                                 ")
            print("--------------------------------------------------------------------------------------------------")
            for i in range(len(names)):
                print(names[i], "| Finished in",total_timer[int(i)],"seconds","| Score:",score[i],remarks[i])
            print("--------------------------------------------------------------------------------------------------")
            print("                                MIND MASTERS v1.0.0beta                                           ")
            print("--------------------------------------------------------------------------------------------------")
            print()
    else:
        break       
    repeat_loop = input("Go Back to Main Menu? (Y/N): ").upper()
    time.sleep(1)
    print()
    print()
    if repeat_loop == "N":
        game_running = False
        print()



