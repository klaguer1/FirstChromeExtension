import boto3 
from boto3.dynamodb.conditions import Key 

RESTAURANTS = [
    {"name": "Frankensons Pizzeria"}, {"name": "Sista Kims"}, {"name": "Eat Your Heart Out Food Hall"},
    {"name": "Houston Boudin Ball"}, {"name": "360 With Speedy"}, {"name": "Vibes"},
    {"name": "Bruckner Pizza"}, {"name": "Tamarind Island"}, {"name": "Aunts Et Uncle"},
    {"name": "Taste Of Heaven"}, {"name": "New York Pizza"}, {"name": "Taste Budz Deli"},
    {"name": "Houston Food Tour"}, {"name": "Mezza Grille"}, {"name": "The Waffle Bus"},
    {"name": "The Better Box"}, {"name": "Cool Runnings"}, {"name": "The Puddery"},
    {"name": "The Breakfast Klub Houston"}, {"name": "Butter Funk Kitchen"}, {"name": "Stick Talk"},
    {"name": "Mac & Cheese & Collard Greens Recipe"}, {"name": "La Barbcao"}, {"name": "Next stop on the food tour"},
    {"name": "Grandma Hannahs Soul Truck"}, {"name": "Mad House Coffee"}, {"name": "Wi Jammin Carribean Cafe"},
    {"name": "Joy Burgers"}, {"name": "Cracker Barell"}, {"name": "The Meat Wagon"},
    {"name": "Ranking Everything At DisneyLand"}, {"name": "Disney Land Pickle"}, {"name": "Ice Cream Cart"},
    {"name": "Roscoes Famous Deli"}, {"name": "Uno Katsu Sando"}, {"name": "Detroit & Chicago Food Tour update"},
    {"name": "New Honey Pepper Pimento Chicken Sandwich"}, {"name": "Cleo’s Southern Cuisine"},
    {"name": "Chicago Chicken"}, {"name": "Soul Prime Chicago"}, {"name": "Hoodbachi"},
    {"name": "Detroit 75 Kitchen"}, {"name": "Whatcha Wanna EAT Food Hall"}, {"name": "The Spot Truk"},
    {"name": "Speedy’s Coney Island"}, {"name": "Food Tour 2nd Stop Announcement"}, {"name": "Top Of The World"},
    {"name": "Glaze Doughnuts 48 Hour"}, {"name": "Glaze Doughnuts"}, {"name": "Milpa"},
    {"name": "Picanha Steak Restaurant"}, {"name": "The Wood Ubran Kitchen & Sports Lounge"}, {"name": "Jazzy’s Kitchen"},
    {"name": "Blaze Pizza"}, {"name": "Layla Grill & Hookah"}, {"name": "Mr.Beast fight"},
    {"name": "Shang Mian Noodels"}, {"name": "Bobby’s Burgers"}, {"name": "Unko Frank’s Hawaiian BBQ"},
    {"name": "Wingstop Latto Wings"}, {"name": "Truffles And Bacon"}, {"name": "Kraken Cafe"},
    {"name": "Citrus Grill & Hookah"}, {"name": "Ole Churros"}, {"name": "Houston TX Hot Chicken 3"},
    {"name": "Aroma Latin Cocina 7 Month"}, {"name": "Bjs Restaurant And Brewhouse"},
    {"name": "Starburst Parlor Keto Bakery"}, {"name": "Lefts J’s"}, {"name": "Taco Man Grill"},
    {"name": "Family Snow Cone"}, {"name": "Doanburi Premium Sushi"}, {"name": "Humo Barbecue"},
    {"name": "Wingstop Secret Flavor"}, {"name": "Tacos El Gordo"}, {"name": "Cinnaholic"},
    {"name": "Bellagio Bakery"}, {"name": "Pretty Soul Kitchen"}, {"name": "Dynamite Korean St Food & Sushi/Grill"},
    {"name": "Shanghai Plaza"}, {"name": "Family Sneaker Fun Day"}, {"name": "Doanburi Premium Sushi And Catering"},
    {"name": "Buldogis Gourmet Hot Dogs"}, {"name": "Le Cafe Du Sud"}, {"name": "The Bao Spot 24 Hour Update"},
    {"name": "The Bao Spot"}, {"name": "Keiths Stuffed Salmon"}, {"name": "Disney Epcot"}, {"name": "Chicken Fire"},
    {"name": "PaPa G’s Freeze Shop"}, {"name": "Home Cooked Soul Food"}, {"name": "World Food Trucks"},
    {"name": "Disney World Magic Kingdom"}, {"name": "Disney Springs In Orlando, Fl"}, {"name": "Gideons"},
    {"name": "Hart House"}, {"name": "Undisclosed Brunch Location"}, {"name": "Universal Studios"},
    {"name": "DayBird $80 Kaluga Cavier Fish Sandwich"}, {"name": "LA Taco Stand"}, {"name": "Keith Lee DoorDash Hack"},
    {"name": "Gäbi Coffee & Bakery"}, {"name": "Aloha Mamacita 2 month Update"}, {"name": "Catchers Fish House Update"},
    {"name": "Catchers Fish House"}, {"name": "La Chilanga Mexican Food"}, {"name": "Le Cafe De Sud"},
    {"name": "Karved"}, {"name": "Nerdy Nuts"}, {"name": "Chipotle"}, {"name": "Thick & Thin"},
    {"name": "Wingstop 4/20 Hot Box"}, {"name": "STK Steakhouse"}, {"name": "Houston Hot Chicken"},
    {"name": "Target & Trader Joes"}, {"name": "Bath Day From Cesar"}, {"name": "Lo-Lo’s Chicken & Waffles 2"},
    {"name": "Testimony Neighbor Story (from our YT Vlog)"}, {"name": "The X Pot"},
    {"name": "Testimony The Days I live for"}, {"name": "Family Dentist Day with Ron"}, {"name": "The Coffee Class"},
    {"name": "Life update + Chipotle"}, {"name": "Sorry Not Sorry Creamery family"}, {"name": "Secret Pizza"},
    {"name": "Pink Potato 24 Hour Update"}, {"name": "The Pink Potato"}, {"name": "Harolds Chicken vs Uncle Remus Mild Sauce"},
    {"name": "Tacos Los Toritos"}, {"name": "Popeyes Strawberry Biscuit"}, {"name": "Oxtail & Fufu with toosii"},
    {"name": "Spend the day with me"}, {"name": "Chipotle NEW favorite way to eat a Fajita Quesadilla"},
    {"name": "Happy birthday baby"}, {"name": "The Cookie Jar Bar"},
    {"name": "How Do You Stay Fit While Eating So Much? Keith Speaks"}, {"name": "Blue Saigon Attempt 1"},
    {"name": "Kyleighs Lemonade"}, {"name": "Testimony Psalms 23 forever and always"}, {"name": "Nerdy Nuts"},
    {"name": "ChinaLatina By Chef Beni Story time"}, {"name": "Five Guys Fry Sauce"}, {"name": "Cocoa Asante"},
    {"name": "Smoke & Fire Blueberry Chicken Sandwich"}, {"name": "Chipotle"}, {"name": "Mama Bird"},
    {"name": "Chil Fil-A hack update"}, {"name": "Wingstop New Flavors"}, {"name": "Salmon Dinner W/ Mango Salsa"},
    {"name": "Chic Fil-A hack"}, {"name": "Sushi & Joy"}, {"name": "Stuffed Salmon Rolls & Garlic Bacon Mashed Potatoes"},
    {"name": "Best Friend By Roi Choi"}, {"name": "GYU+"}, {"name": "Sweets Raku"}, {"name": "Shang Artisan Noodle"},
    {"name": "Taking Over Vegas today with Chipotle"}, {"name": "Papi’s Tacos And Churro’s"},
    {"name": "Kids Choice Awards Event food"}, {"name": "Chipotle The Keithadilla is in the chipotle app WITH the vinaigrette"},
    {"name": "with mario lopez"}, {"name": "Half Bird Chicken & Beer"}, {"name": "Ranking Foreign Snacks 1-9"},
    {"name": "Starbucks & Girl Scout Cookies"}, {"name": "Access Hollywood"},
    {"name": "24 hour update on Dynamite Korean St Food & Sushi/Grill & AHAV"},
    {"name": "Dynamite Korean St Food & Sushi/Grill"}, {"name": "AHAV"}, {"name": "Philly’s Best in Burbank CA"},
    {"name": "Dominos"}, {"name": "Pepper Club part 3"}, {"name": "Pepper Club"}
]

print('apple')

def query_reviews(book_id, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')

    reviewsTable = dynamodb.Table('KeithLeeReviews')

    response = reviewsTable.query(
        KeyConditionExpression=Key('id').eq(1)
    )
    return response['Items']
def add_places_visited(dynamodb=None): 
    # Define the list of restaurant objects
    dynamodb = boto3.resource('dynamodb')
    reviewsTable = dynamodb.Table('KeithLeeReviews')


# Insert restaurant objects into the DynamoDB table
    counter=2
    for restaurant in RESTAURANTS:
        reviewsTable.put_item(
            TableName="KeithLeeReviews",
            Item={
                'id': counter,
                'restaurantName':  restaurant['name']
            }
        ) 
        counter+=1

print("Restaurant objects inserted successfully!")
if __name__ == '__main__':
    add_places_visited()
    query_id = 10
    print(f"ID: {query_id}")
    reviews_data = query_reviews(query_id)
    for data in reviews_data:
       print(data['id'], ":", data['restaurantName'])