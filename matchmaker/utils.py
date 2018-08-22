GENDER_CHOICES =(('Male', 'Male'),('Female', 'Female'))
LANGUAGE_CHOICES = (('en,English','en,English'),
('ru,Russian','ru,Russian'),
('es,Spanish','es,Spanish'),
('br,Portuguese','br,Portuguese'),
('tr,Turkish','tr,Turkish'),
('fr,French','fr,French'),
('id,Indonesian','id,Indonesian'),
('se,Swedish','se,Swedish'),
('tlTagalog','tlTagalog'),
('vi,Vietnamese','vi,Vietnamese'),
('it,Italian','it,Italian'),
('zh,Chinese','zh,Chinese'),
('hi,Hindi','hi,Hindi'),
('Ethnicity','Ethnicity'),)

ETHINICITY_CHOICES =(('Black/African descent','Black/African descent'),
('Pacific islander','Pacific islander'),
('Indian','Indian'),
('White/Caucasian','White/Caucasian'),
('Mixed','Mixed'),
('Middle eastern','Middle eastern'),
('Asian','Asian'),
('Other','Other'),
('Native american','Native american'),
('Latino/ hispanic','Latino/ hispanic'),)


RELIGION_CHOICES = (('Hindu','Hindu'),
('Buddhist','Buddhist'),
('Agnostic','Agnostic'),
('Spiritual','Spiritual'),
('Orthodox','Orthodox'),
('Catholic','Catholic'),
('Atheist','Atheist'),
('Other','Other'),
('Jewish','Jewish'),
('Protestant','Protestant'),
('Christian','Christian'),
('Muslim','Muslim'),)

SIGN_CHOICES =(('Sagittarius','Sagittarius'),
('Virgo','Virgo'),
('Gemini','Gemini'),
('Pisces','Pisces'),
('Capricorn','Capricorn'),
('Libra','Libra'),
('Cancer','Cancer'),
('Aries','Aries'),
('Scorpio','Scorpio'),
('Leo','Leo'),
('Taurus','Taurus'),
('Aquarius','Aquarius'),)


BODY_TYPE_CHOICES =(('A little extra','A little extra'),
('Fit','Fit'),
('Full-figured','Full-figured'),
('Average','Average'),
('Better not say','Better not say'),
('Curvy','Curvy'),
('Overweight','Overweight'),
('Thin','Thin'),)



SEXUAL_ORIENTATION_CHOICES =(('Straight','Straight'),
('Bisexual','Bisexual'),	
('Gay','Gay'),)

REL_STATUS_CHOICES = (('In an open relationship','In an open relationship'),
('Single','Single'),
('Tell you later','Tell you later'),
('Seeing someone','Seeing someone'),
('Married','Married'),
('Widowed','Widowed'),
('Divorced','Divorced'),
('Separated','Separated'),)

REL_TYPE_CHOICES =(('Monogamous','Monogamous'),
('Polygamous','Polygamous'),)



CHILDREN_CHOICES = (('Expecting','Expecting'),
('Want kids','Want kids'),
('Have kids','Have kids'),
("Don't want kids","Don't want kids"),
('No kids','No kids'),
('Someday','Someday'),
('Might want kids','Might want kids'),)

PETS_CHOICES = (('Other','Other'),
('Hate pets','Hate pets'),
('Dogs','Dogs'),
('Cats','Cats'),)




CAR_CHOICES = ((False,"I don't have one"),
(True,'I have my own car'),)


HOME_OWNERSHIP_CHOICES = (('Live in a dormitory','Live in a dormitory'),
('Own a house/apartments','Own a house/apartments'),
('Share a flat','Share a flat'),
('Rent a house/apartments','Rent a house/apartments'),
('Live with parents','Live with parents'),)


PROFESSION_CHOICES = (('College student','College student'),
('Homemaker','Homemaker'),
('Apprentice','Apprentice'),
('Retired','Retired'),
('Employee','Employee'),
('Self-employed','Self-employed'),
('Civil servant','Civil servant'),
('Unemployed','Unemployed'),)


INDUSTRY_CHOICES = (('Science','Science'),
('Non-profit','Non-profit'),
('Health care','Health care'),
('Education','Education'),
('Arts/music/writing','Arts/music/writing'),
('Technology','Technology'),
('Sales/marketing','Sales/marketing'),
('Hospitality','Hospitality'),
('Entertainment/media','Entertainment/media'),
('Business management','Business management'),
('Transportation','Transportation'),
('IT','IT'),
('Military','Military'),
('Government/politics','Government/politics'),
('Construction','Construction'),)


EDUCATION_CHOICES = (('College','College'),
("I'm just very smart","I'm just very smart"),
('Post grad','Post grad'),
('Secondary education','Secondary education'),
('Not finished','Not finished'),
('University','University'),
('Apprenticeship','Apprenticeship'),
('Advanced degree','Advanced degree'),)




SMOKING_CHOICES = (('Only with alcohol','Only with alcohol'),
('Social smoker','Social smoker'),
('Trying to quit','Trying to quit'),
('Non-smoker','Non-smoker'),
('Quit','Quit'),
('Smoker','Smoker'),)


DRINKING_CHOICES = (('Drinking','	Drinking'),
('Sometimes','Sometimes'),
('Socially','Socially'),
('Never','Never'),
('Often','Often'),)

DRUG_CHOICES =  (('Often','Often'),
('Never','Never'),
('Sometimes','Sometimes'),)


DIET_CHOICES = (('Vegan','Vegan'),
('Kosher','Kosher'),
('I eat meat','I eat meat'),
('Halal','Halal'),
('Vegetarian','Vegetarian'),)




def create_dummyUsers():
	from .models import User
	from faker import Faker
	fake = Faker()
	user_exist = True
	for n in range(1,5001):
		while user_exist:
			profile = fake.simple_profile()
			email = 'daahrmmieboiye+' + profile['mail'].split('@')[0] + '@gmail.com'
			user_exist = User.objects.filter(email=email).exists()
			user_exist  = User.objects.filter(username=(profile['username']).lower().strip()).exists()
			if profile['sex'] == 'M':
				gender = GENDER_CHOICES[0][0]
			elif profile['sex'] == 'F':
				gender = GENDER_CHOICES[1][0]
		if (not user_exist) and (not('.' in profile['name'])) and (len((profile['name']).split(' ')) == 2):
			name = (profile['name']).split(' ')
			user = User.objects.create_user(
				first_name = name[0],
				last_name = name[1],
				gender = gender,
				username = (profile['username']).lower().strip(),
				email = email,
				date_of_birth = profile['birthdate'],
				password = 'ps_123456')
			user.profile.about = fake.text(max_nb_char=160)
			user.profile.save()
		user_exist=True


def create_interests():
	from .models import Category, Interest
	allinterestlists = ['Films and TV Series',
				'Comedy',
				'Action',
				'Adventure',
				'Drama',
				'Romantic',
				'comedy',
				'Documentary',
				'Horror',
				'Science',
				'fiction',
				'Fantasy',
				'Historical',
				'Animated',
				'films',
				'Musicals',
				'Police',
				'drama',
				'Cartoons',
				'Arthouse',
				'Thriller',
				'Discovery',
				'Anime',
				'Crime',
				'drama',
				'Melodrama',
				'Reality show',],['Listening to Music',
				'Pop-rock',
				'R n B',
				'Dance and DJ Soul',
				'Rock',
				'Classical/opera',
				'Blues',
				'Jazz',
				'Country',
				'Soundtracks',
				'Hard rock',
				'Rap',
				'Electronic/techno',
				'Disco',
				'Metal',
				'Pop',
				'Grunge',
				'Hip-Hop',], ['Games',
				'Computer games',
				'Table-top games',
				'Quests',
				'Adventure',], ['Books',
				'Ancient literature',
				'Medieval prose',
				'Biographical fiction',
				'Historical fiction',
				'Horoscopes/fortune telling',
				'Business literature',
				'Detective story',
				'Fairy tales',
				'Lyrics',
				'Poetry',
				'Romance Science and Technology',
				'Mystic',
				'Adventure',
				'Psychological prose',
				'Science fiction',
				'Philosophy',
				'Fantasy',], ['Sports',
				'Hiking',
				'Fitness training',
				'American football',
				'Jogging',
				'Cycling',
				'Swimming',
				'Тennis',
				'Rugby',
				'Skiing',
				'Snowboarding',
				'Boxing',
				'Wrestling',
				'Billiards / pool',
				'Badminton',
				'Gym / body building',
				'Table tennis',
				'Rock climbing',
				'Soccer',
				'Basketball',
				'Volleyball',
				'Chess',
				'Fencing',
				'Wakeboarding',
				'Surfing',
				'Diving',
				'Kayaks',
				'Horseback riding',], ['Pets',
				'Dogs',
				'Cats',
				'Rabbits',
				'Hamsters',
				'Iguana',
				'Parrot',
				'Ferret',
				'Turtle',
				'Guinea Pig',
				'Fish',
				'Chinchilla',
				'Ant farm',
				'Frog',
				'Mouse',
				'Pig',
				'Rat Salamander',], ['Style',
				'Sophisticated',
				'Trendy',
				'Business',
				'Classical',
				'Cool',
				'Rock',
				'Sporty',
				'Casual',], ['Hobby',
				'Reading',
				'Watching TV',
				'Going to Movies',
				'Fishing',
				'Computer',
				'Gardening',
				'Walking',
				'Listening to Music',
				'Hunting',
				'Team',
				'Sports',
				'Shopping',
				'Traveling',
				'Socializing',
				'Playing',
				'Music',
				'Crafts',
				'Watching sports',
				'Sport activities',
				'Cooking',
				'Camping',
				'Art work',
				'Animal Care',
				'Bowling',
				'Theater',
				'Billiards',
				'Volunteer Work',], ['Travelling',
				'Adventure',
				'Cruising (maritime)‎',
				'Business tourism',
				'Safari holidays',
				'Hitch-hiking',
				'Bicycle tours‎ ‎',
				'Ecotourism‎',
				'Food tourism',
				'Domestic tourism',
				'Excursions',
				'Extreme tourism',
				'Motorcycle touring',
				'Self-guided tour',
				'Sports tourism',
				'Walking tour',
				'Wildlife tourism',], ['Inspiration',
				'Time on your own',
				'Communication',
				'Family time',
				'Art',
				'Sports',
				'Adventure',
				'Nature',
				'Fiction',
				'Business literature',
				'Listening to Music',
				'Meditation',
				'Working',
				'Science',
				'Movies',
				'Self-education',
				'Success stories',], ['People',
				'No preference',
				'Adventurous',
				'Confident',
				'Easy going',
				'Funny',
				'Generous',
				'Helpful',
				'Reliable',
				'Reserved',
				'Sensitive',
				'Thoughtful',
				'Athletic',
				'Attractive',
				'Balanced',
				'Freethinking',
				'Honest',
				'Independent',
				'Individualistic',
				'Kind',
				'Leaderly',
				'Optimistic',]
	for interestlist in allinterestlists:
		cat = interestlist.pop(0)
		cat = Category.objects.create(name=cat)
		for interest in interestlist:
			Interest.objects.create(name=interest, category=cat)


def addRandomUserInterests():
	import random
	from .models import User, Interest
	interestCount = Interest.objects.count()
	for user in User.objects.all():
		for n in range(1, random.randint(4, 20)):
			pick  = random.randint(1, interestCount)
			try:
				interest = Interest.objects.get(id=pick)
				user.profile.interests.add(interest)
			except Exception as e:
				print('Error', e)