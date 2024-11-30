import streamlit as st
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from bs4 import BeautifulSoup  
import requests
import webbrowser
import plotly.express as px
import base64
from streamlit_option_menu import option_menu
# ... (rest of your code remains unchanged)
def load_prep(img_bytes):
    img = tf.image.decode_image(img_bytes, channels=3)
    img = tf.image.resize(img, size=(224, 224))
    return img

# Class names for prediction
class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
               'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
               'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
               'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
               'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
               'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
               'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
               'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
               'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
               'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
               'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
# Function to search and display images based on a query using Google Images
def search_and_display_images(query, num_images=20):
    try:
        # Initialize an empty list for image URLs
        k=[]  
        # Initialize an index for iterating through the list of images
        idx=0  
        # Construct Google Images search URL
        url = f"https://www.google.com/search?q={query}&tbm=isch"  
         # Make an HTTP request to the URL
        response = requests.get(url) 
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")  
        # Initialize an empty list for storing image URLs
        images = []  
        # Iterate through image tags in the HTML content
        for img in soup.find_all("img"):  
             # Limit the number of images to the specified amount
            if len(images) == num_images: 
                break
            # Get the image source URL
            src = img.get("src")  
            # Check if the source URL is valid
            if src.startswith("http") and not src.endswith("gif"):  
                # Add the image URL to the list
                images.append(src)  
        # Iterate through the list of image URLs
        for image in images:  
            # Add each image URL to the list 'k'
            k.append(image)  
        # Reset the index for iterating through the list of image URLs
        idx = 0  
        # Iterate through the list of image URLs
        while idx < len(k):
            # Iterate through the columns in a 4-column layout 
            for _ in range(len(k)): 
                # Create 4 columns for displaying images 
                cols = st.columns(4)  
                # Display the first image in the first column
                cols[0].image(k[idx], width=150)  
                idx += 1 
                # Move to the next image in the list
                cols[1].image(k[idx], width=150)
                # Display the second image in the second column
                idx += 1  
                # Move to the next image in the list
                cols[2].image(k[idx], width=150)  
                # Display the third image in the third column
                idx += 1  
                # Move to the next image in the list
                cols[3].image(k[idx], width= 150)  
                # Display the fourth image in the fourth column
                idx = idx + 1  
                # Move to the next image in the list
    except:
         # Handle exceptions gracefully if there is an error while displaying images
        pass
# Function to create a home page

# Function to create a page for displaying plant name and treatment
def show_plant_info(predicted_value):
    st.subheader("Plant Name:")
    lis=predicted_value.split('___')
    st.write(lis[0])
    if lis[-1]=='healthy':
        st.markdown("### Plant is Healthy")
    else:
        st.markdown("### Plant is Unhealthy and Disease is detected")  
        if predicted_value=='Apple___Apple_scab':
            st.markdown("Apple scab is a serious disease that affects apples and crabapples, as well as other plants in the same family. It occurs everywhere where apples are grown around the world and causes more damage than any other apple disease. However, the disease is more common in areas that have cool, wet spring weather.")
            st.markdown("##### Treatment: Managing and treating the apple scab fungus is an integrated process that combines sanitation, resistant cultivars, and fungicides.")
            st.markdown("Choose Scab-Resistant Cultivars such as:")
            st.markdown("Crimson Crisp")
            st.markdown("Crimson Gold")
            st.markdown("Enterprise")
            st.markdown("Freedom\nGoldrush")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.planetnatural.com/pest-problem-solver/plant-disease/apple-scab/")
            st.markdown("### Images of Apple scab")
            search_and_display_images('Apple scab in apple',num_images=20)
        elif predicted_value=='Apple___Black_rot':
            st.markdown("Black rot is a fungal disease affecting apple trees, caused by the pathogen Venturia inaequalis. This disease is a significant concern for apple growers as it can lead to severe fruit loss if not properly managed. Black rot primarily affects the leaves, fruit, and occasionally, the twigs of apple trees.")
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/black-rot/")    
            st.markdown("#### Remedy : As with many other diseases, sanitation is one of the major factors.")
            st.markdown("Remove mummified fruit, dead trees, dead or dying infected limbs. Prune out cankersto greatly reduce the amount of available inoculum. For homeowners, black rot can be controlled by starting a full-rate protectant spray program early in the season with copper-based products, lime-sulfur or Daconil.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://extension.wvu.edu/lawn-gardening-pests/plant-disease/tree-fruit-disease/black-rot-disease-in-apples#:~:text=Remove%20mummified%20fruit%2C%20dead%20trees,%2C%20lime%2Dsulfur%20or%20Daconil.")
            st.markdown("### Images of Black rot")
            search_and_display_images('Black rot in apple',num_images=20)
        elif predicted_value=='Apple___Cedar_apple_rust':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/cedar-apple-rust/")
            st.markdown("Cedar apple rust is a fungal disease that requires juniper plants to complete its complicated two year life-cycle. The fungus spends a portion of its life on the juniper plant, and the rest on apple or crabapple trees. It is most damaging to apples and crabapples.")
            st.markdown("#### Remedy : On apple and crab-apple trees, look for pale yellow pinhead sized spots on the upper surface of the leaves shortly after bloom.")
            st.markdown("1. Choose resistant cultivars when available.")
            st.markdown("2. Rake up and dispose of fallen leaves and other debris from under trees.")
            st.markdown("3. Remove galls from infected junipers. In some cases, juniper plants should be removed entirely.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.planetnatural.com/pest-problem-solver/plant-disease/cedar-apple-rust/")
            st.markdown("### Images of Cedar apple rust")
            search_and_display_images('Cedar apple rust in apple',num_images=20)
        elif predicted_value=='Cherry_(including_sour)___Powdery_mildew':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/powdery-mildew/")
            st.markdown("Powdery mildew is a fungal disease that affects a wide range of plants. Powdery mildew diseases are caused by many different species of fungi in the order Erysiphales, with Podosphaera xanthii (a.k.a. Sphaerotheca fuliginea) being the most commonly reported cause.")
            st.markdown("#### Remedy : Unlike many other fungal diseases you might have come across, this one spreads and thrives the most in dry and warm climates.")
            st.markdown("1. Plant resistant cultivars in sunny locations whenever possible.")
            st.markdown("2. Prune or stake plants to improve air circulation.")
            st.markdown("3. Water in the morning, so plants have a chance to dry during the day.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.planetnatural.com/pest-problem-solver/plant-disease/powdery-mildew/")
            st.markdown("### Images of Powdery mildew")
            search_and_display_images('Powdery mildew in cherry',num_images=20)
        elif predicted_value=='Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/corn-gray-leaf-spot/")
            st.markdown("Gray leaf spot is a foliar disease that affects corn, a staple crop grown throughout the United States. The disease is caused by the fungus Cercospora zeae-maydis. The disease is most severe in warm, humid climates and where corn is grown continuously.")
            st.markdown("#### Remedy : Gray leaf spot lesions begin as small necrotic pinpoints.")
            st.markdown("1. Cultural Practices.")
            st.markdown("2. Hybrid Resistance.")
            st.markdown("3. Fungicides.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.pioneer.com/us/agronomy/gray_leaf_spot_cropfocus.html")
            st.markdown("### Images of Gray leaf spot")
            search_and_display_images('Gray leaf spot in corn',num_images=20)
        elif predicted_value=='Corn_(maize)___Common_rust_':
            st.markdown("Common rust is a foliar disease that affects corn, a staple crop grown throughout the United States. The disease is caused by the fungus Puccinia sorghi and is most severe in warm, humid climates and where corn is grown continuously.")
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/corn-rust/")
            st.markdown("#### Remedy : This disease is caused by fungus.")
            st.markdown("1. Plant resistant varieties available locally.")
            st.markdown("2. Plant early to avoid optimal conditions for infection.")
            st.markdown("3. Use shorter season varieties that mature earlier.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://plantix.net/en/library/plant-diseases/100082/common-rust-of-maize/")
            st.markdown("### Images of Common rust")
            search_and_display_images('Common rust in corn',num_images=20)
        elif predicted_value=='Corn_(maize)___Northern_Leaf_Blight':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/corn-blight/")
            st.markdown("Northern corn leaf blight is a foliar disease that affects corn, a staple crop grown throughout the United States. The disease is caused by the fungus Exserohilum turcicum and is most severe in temperate and subtropical climates.")
            st.markdown("#### Remedy : Effective management practices that reduce the impact of NCLB include selecting resistant hybrids, reducing corn residue, timely planting, and applying foliar fungicides.")
            st.markdown("1. Choose Resistant Hybrids.")
            st.markdown("2. Reduce Previous Corn Residue.")
            st.markdown("3. Plant Timely.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.pioneer.com/us/agronomy/Managing-Northern-Corn-Leaf-Blight.html")
            st.markdown("### Images of Northern corn leaf blight")
            search_and_display_images('Northern corn leaf blight in corn',num_images=20)
        elif predicted_value=='Grape___Black_rot':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/black-rot/")
            st.markdown("Black rot is a fungal disease affecting grape trees, caused by the pathogen Venturia inaequalis. This disease is a significant concern for grape growers as it can lead to severe fruit loss if not properly managed. Black rot primarily affects the leaves, fruit, and occasionally, the twigs of grape trees.")
            st.markdown("#### Remedy : Infected prunings and mummified berries should be removed, burned, and/or buried in the soil before new growth begins in the spring.")
            st.markdown("1. apply a fungicide every 14 days.")
            st.markdown("2.  During long rainy periods, shorten the interval to 7 to 10 days between sprays.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://extension.psu.edu/black-rot-on-grapes-in-home-gardens")
            st.markdown("### Images of Black rot")
            search_and_display_images('Black rot in grape',num_images=20)
        elif predicted_value=='Grape___Esca_(Black_Measles)':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/esca-black-measles/")
            st.markdown("Esca, also known as black measles, is a fungal disease that affects grape trees. It is a significant concern for grape growers as it can lead to severe fruit loss if not properly managed. Esca primarily affects the leaves, fruit, and occasionally, the twigs of grape trees.")
            st.markdown("#### Remedy : Wine grape growers with small vineyards will often have field crews remove infected fruit prior to harvest.")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://grapes.extension.org/grapevine-measles/")
            st.markdown("### Images of Esca")
            search_and_display_images('Esca in grape',num_images=20)
        elif predicted_value=='Grape___Leaf_blight_(Isariopsis_Leaf_Spot)':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/leaf-blight/")
            st.markdown("Leaf blight is a fungal disease that affects grape trees. It is a significant concern for grape growers as it can lead to severe fruit loss if not properly managed. Leaf blight primarily affects the leaves, fruit, and occasionally, the twigs of grape trees.")
            st.markdown("#### Remedy : Generally, vines should be grown in full sun, in a well draining soil and in a location where there is good circulating air to reduce incidence of disease.")
            st.markdown("1. Plant less susceptible cultivars.")
            st.markdown("2. do not over fertilize.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://plantvillage.psu.edu/topics/grape/infos")
            st.markdown("### Images of Leaf blight")
            search_and_display_images('Leaf blight in grape',num_images=20)
        elif predicted_value=='Orange___Haunglongbing_(Citrus_greening)':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/citrus-greening/")  
            st.markdown("Citrus greening, also known as Huanglongbing (HLB) or yellow dragon disease, is a disease caused by a fastidious, phloem-limited bacterium called Candidatus Liberibacter asiaticus. Citrus is the most economically important fruit crop in the world, so citrus greening is a huge concern.")
            st.markdown("#### Remedy : The symptoms of citrus greening are many and can easily be seen on an infected tree.")
            st.markdown("1. Observe the plants with Leaf yellowing.")
            st.markdown("2. Remove misshapen fruits")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://study.com/academy/lesson/citrus-greening-disease-symptoms-treatment.html")
            st.markdown("### Images of Citrus greening")
            search_and_display_images('Citrus greening in orange',num_images=20)
        elif predicted_value=='Peach___Bacterial_spot':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/bacterial-spot/")
            st.markdown("Bacterial spot is a common disease affecting peach trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : A few chemical control options are available for use in the home orchard, so homeowners should select varieties that resist bacterial spot.")
            st.markdown("1. Early season pruning can help control tree vigor.")
            st.markdown("2. Fertilize trees.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.aces.edu/blog/topics/crop-production/bacterial-spot-treatment-in-peaches/")
            st.markdown("### Images of Bacterial spot")
            search_and_display_images('Bacterial spot in peach',num_images=20)
        elif predicted_value=='Pepper,_bell___Bacterial_spot':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/bacterial-spot/")
            st.markdown("Bacterial spot is a common disease affecting pepper trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : The best management of pepper bacterial leaf spot can be achieved through an integrated strategy because it’s been found that a single measure, such as seed treatment, did not adequately control bacterial spot.")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://extension.wvu.edu/lawn-gardening-pests/plant-disease/fruit-vegetable-diseases/bacterial-leaf-spot-of-pepper#:~:text=Copper%20sprays%20can%20be%20used,good%20protection%20from%20the%20disease.")
            st.markdown("### Images of Bacterial spot")
            search_and_display_images('Bacterial spot in pepper',num_images=20)
        elif predicted_value=='Potato___Early_blight':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/early-blight/")
            st.markdown("Early blight is a common disease affecting potato trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : Early blight overwinters on infected plant tissue and is spread by splashing rain, irrigation, insects and garden tools.")
            st.markdown("1. Prune or stake plants to improve air circulation and reduce fungal problems.")
            st.markdown("2. Make sure to disinfect your pruning shears (one part bleach to 4 parts water) after each cut.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.planetnatural.com/pest-problem-solver/plant-disease/early-blight/")
            st.markdown("### Images of Early blight")
            search_and_display_images('Early blight in potato',num_images=20)
        elif predicted_value=='Potato___Late_blight':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/late-blight/")
            st.markdown("Late blight is a common disease affecting potato trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : Unlike other fungal diseases, this plant problem does not overwinter in the soil or on garden.")
            st.markdown("1. Plant resistant cultivars when available.")
            st.markdown("2. Water in the early morning hours.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.planetnatural.com/pest-problem-solver/plant-disease/late-blight/")
            st.markdown("### Images of Late blight")
            search_and_display_images('Late blight in potato',num_images=20)
        elif predicted_value=='Squash___Powdery_mildew':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/powdery-mildew/")
            st.markdown("Powdery mildew is a fungal disease that affects a wide range of plants. Powdery mildew diseases are caused by many different species of fungi in the order Erysiphales, with Podosphaera xanthii (a.k.a. Sphaerotheca fuliginea) being the most commonly reported cause.")
            st.markdown("#### Remedy :  It requires high relative humidity to spread.")
            st.markdown("1. Plant resistant cultivars in sunny locations whenever possible.")
            st.markdown("2. Water in the morning, so plants have a chance to dry during the day.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.planetnatural.com/pest-problem-solver/plant-disease/powdery-mildew/")
            st.markdown("### Images of Powdery mildew")
            search_and_display_images('Powdery mildew in sqaush',num_images=20)
        elif predicted_value=='Strawberry___Leaf_scorch':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/leaf-scorch/")
            st.markdown("Leaf scorch is a common disease affecting strawberry trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : When making new plantings always ensure that good planting practices are implemented.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.gardeningknowhow.com/edible/fruits/strawberry/strawberries-with-leaf-scorch.htm")
            st.markdown("### Images of Leaf scorch")
            search_and_display_images('Leaf scorch in Strawberry',num_images=20)
        elif predicted_value=='Tomato___Bacterial_spot':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/bacterial-spot/")
            st.markdown("Bacterial spot is a common disease affecting tomato trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : To keep leaves dry and to prevent the spread of the pathogens, avoid overhead watering.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://hort.extension.wisc.edu/articles/bacterial-spot-of-tomato/")
            st.markdown("### Images of Bacterial spot")
            search_and_display_images('Bacterial spot in Tomato',num_images=20)
        elif predicted_value=='Tomato___Early_blight':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/early-blight/")
            st.markdown("Early blight is a common disease affecting tomato trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : Early blight overwinters on infected plant tissue and is spread by splashing rain, irrigation, insects and garden tools.")
            st.markdown("1. Prune or stake plants to improve air circulation and reduce fungal problems.")
            st.markdown("2. Burn or bag infected plant parts.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.planetnatural.com/pest-problem-solver/plant-disease/early-blight/")
            st.markdown("### Images of Early blight")
            search_and_display_images('Early blight in Tomato',num_images=20)
        elif predicted_value=='Tomato___Late_blight':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/late-blight/")
            st.markdown("Late blight is a common disease affecting tomato trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : Unlike other fungal diseases, this plant problem does not overwinter in the soil or on garden.")
            st.markdown("1. Plant resistant cultivars when available.")
            st.markdown("2. Water in the early morning hours.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.planetnatural.com/pest-problem-solver/plant-disease/late-blight/")
            st.markdown("### Images of Late blight")
            search_and_display_images('Late blight in Tomato',num_images=20)
        elif predicted_value=='Tomato___Leaf_Mold':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/leaf-mold/")
            st.markdown("Leaf mold is a common disease affecting tomato trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : Unlike other fungal diseases, this plant problem does not overwinter in the soil or on garden.")
            st.markdown("1. Plant resistant varieties.")
            st.markdown("2. Water in the early morning hours.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.vegetables.cornell.edu/pest-management/disease-factsheets/tomato-leaf-mold/")
            st.markdown("### Images of Leaf mold")
            search_and_display_images('Leaf mold in Tomato',num_images=20)
        elif predicted_value=='Tomato___Septoria_leaf_spot':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/septoria-leaf-spot/")
            st.markdown("Septoria leaf spot is a common disease affecting tomato trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : There are a few options for treating Septoria leaf spot when it appears; these include:")
            st.markdown("1. Removing Infected Leaves.")
            st.markdown("2. Consider Chemical Fungicides.")
            st.markdown("3. Start With a Clean Garden.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.thespruce.com/identifying-and-controlling-septoria-leaf-spot-of-tomato-1402974")
            st.markdown("### Images of Septoria leaf spot")
            search_and_display_images('Septoria leaf spot in Tomato',num_images=20)
        elif predicted_value=='Tomato___Spider_mites Two-spotted_spider_mite':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/spider-mites/")
            st.markdown("Spider mites are members of the Acari (mite) family Tetranychidae, which includes about 1,200 species. They generally live on the undersides of leaves of plants, where they may spin protective silk webs, and they can cause damage by puncturing the plant cells to feed.")
            st.markdown("#### Remedy : One of the best ways to protect your plants is to check them regularly.")
            st.markdown("1. Prune Your Plants.")
            st.markdown("2. Water Plants Properly.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.planetnatural.com/pest-problem-solver/houseplant-pests/spider-mite-control/")
            st.markdown("### Images of Spider mites")
            search_and_display_images('Spider mites in Tomato',num_images=20)
        elif predicted_value=='Tomato___Target_Spot':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/target-spot/")
            st.markdown("Target spot is a common disease affecting tomato trees, as well as other stone fruits and tomatoes. The disease is caused by the bacteria Xanthomonas campestris pv. pruni. Bacterial spot is most severe in warm, wet weather.")
            st.markdown("#### Remedy : Target spot tomato treatment requires a multi-pronged approach.")
            st.markdown("1. Remove old plant debris at the end of the growing season.")
            st.markdown("2. Rotate crops and don’t plant tomatoes in areas where other disease-prone plants have been located in the past year.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://www.gardeningknowhow.com/edible/vegetables/tomato/target-spot-on-tomatoes.htm")
            st.markdown("### Images of Target spot")
            search_and_display_images('Target spot in Tomato',num_images=20)
        elif predicted_value=='Tomato___Tomato_Yellow_Leaf_Curl_Virus':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/tomato-yellow-leaf-curl/")
            st.markdown("Tomato yellow leaf curl virus (TYLCV) is a viral disease that affects tomatoes and other crops. The disease is spread by the whitefly, Bemisia tabaci. TYLCV is found in tropical and subtropical regions around the world.")
            st.markdown("#### Remedy : Strategies to effectively manage the disease include:")
            st.markdown("1. Plant immediately after any tomato-free period or true winter season.")
            st.markdown("2. Remove and destroy old crop.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://ipm.ucanr.edu/agriculture/tomato/tomato-yellow-leaf-curl/")
            st.markdown("### Images of Tomato yellow leaf curl virus")
            search_and_display_images('Tomato yellow leaf curl virus in Tomato',num_images=20)
        elif predicted_value=='Tomato___Tomato_mosaic_virus':
            #st.markdown("### Treatment: https://www.planetnatural.com/pest-problem-solver/plant-disease/tomato-mosaic-virus/")
            st.markdown("Tomato mosaic virus (ToMV) is a viral disease that affects tomatoes and other crops. The disease is spread by contact with an infected plant’s sap, as well as by mechanical transmission (through contact with contaminated tools or hands).")
            st.markdown("#### Remedy : Strategies to effectively manage the disease include:")
            st.markdown("1. If you have any plants in your garden that you suspect may be infected, remove them immediately to prevent the spread of the virus.")
            st.markdown("2. Make sure to inspect transplants before buying them.")
            st.markdown("For more information on how to treat the disease click below:")
            if st.button("Remedy"):
                webbrowser.open_new_tab("https://blogs.ifas.ufl.edu/stlucieco/2023/03/03/tomato-mosaic-virus-tomv-and-its-management/#:~:text=For%20several%20tomato%20viruses%2C%20there%20are%20cultivars%20that%20are%20resistant.&text=If%20you%20have%20any%20plants,be%20uprooted%20entirely%20and%20burned.")
            st.markdown("### Images of Tomato mosaic virus")
            search_and_display_images('Tomato mosaic virus in Tomato',num_images=20)
        else:
            pass
        # Add code to display specific information for each disease (similar to your existing code)
def home():
    @st.cache_data
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    img = get_img_as_base64("pic_image.jpg")
    #background-image: url("https://wallpapers.com/images/hd/plant-background-dyanc2468gd0s24c.jpg");
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    //background-image: url("https://t4.ftcdn.net/jpg/05/96/53/35/360_F_596533582_UgVp2PyEDGWBx71tKyFm9jvYRnSvVerZ.jpg");
    background-image: url("https://wallpapers.com/images/hd/plant-background-dyanc2468gd0s24c.jpg");
    //background-image: url("https://img.freepik.com/free-photo/tropical-palm-leaves-pattern-background-green-monstera-tree-foliage-decoration-design-plant-with-exotic-leaf-closeup_90220-1135.jpg?size=626&ext=jpg&ga=GA1.1.1412446893.1704672000&semt=ais.jpg");
    background-size: 100%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    </style>"""
    st.markdown(page_bg_img, unsafe_allow_html=True)
    html_content = """
    <h1 style="color: black;"><center>Plant Disease Detection<br> and<br> Diagnosis</center></h1>"""
    st.markdown(html_content, unsafe_allow_html=True)
    # Custom HTML and CSS for layout
    custom_layout = """
        <style>
            .custom-container {
                display: flex;
                justify-content: space-between;
            }
            .main-content {
                height: 40%;
                width: 75%;
                color: black;
            }
            .side-content {
                width: 100%;
                height: 10%;
                background-color: black;
                padding: 20px;
                text-align: justify;
                //border-radius: 10px;
            }
        </style>"""

# Display custom layout
    st.markdown(custom_layout, unsafe_allow_html=True)
# Side content
    st.markdown("<div class='side-content'>At Plant Disease Detection and Diagnosis app, we're dedicated to revolutionizing agriculture through cutting-edge technology. Our platform offers a comprehensive solution for plant disease detection and diagnosis, empowering farmers and growers to safeguard their crops and maximize yields.<br><br> Our platform utilizes image processing and machine learning algorithms to swiftly identify and diagnose potential diseases affecting your plants. Navigate through a user-friendly interface that allows you to effortlessly upload images of your crops, enabling our system to analyze and provide accurate assessments.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
# Streamlit app
def main():
    # Create a simple navigation bar
#pages = ["Home", "Plant Disease Information"]
    #page = st.sidebar.selectbox("Select Page", pages)
    selected3 = option_menu(None, ["Home", "Plant Disease Information"], 
    icons=['house', 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)   
    if selected3 == "Home":
        home()
    elif selected3 == "Plant Disease Information":
        st.title("Disease Detetcion and Remedy")
        #st.markdown('<a name="plant-disease-info"></a>', unsafe_allow_html=True)  # Anchor for navigation
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        if uploaded_file is not None:
            img_bytes = uploaded_file.read()
            st.image(img_bytes, caption="Uploaded Image.", width=400)

            feature_model = load_model('best_plant_model.h5')
            image = load_prep(img_bytes)
            pred = feature_model.predict(tf.expand_dims(image, axis=0))
            predicted_value = class_names[pred.argmax()]

            show_plant_info(predicted_value)

if __name__ == "__main__":
    main()
