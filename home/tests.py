#Login testing starts
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from django.test import LiveServerTestCase

# class LoginTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.driver = webdriver.Chrome()
#         cls.driver.get(cls.live_server_url + "/login.html")
#         cls.driver.maximize_window()

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         super().tearDownClass()

#     def test_login_successful(self):
#         wait = WebDriverWait(self.driver, 20)  # Adjust timeout as needed

#         # Wait for the username input field
#         username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#         password_input = self.driver.find_element(By.NAME, "password")

#         # Input username and password
#         username_input.send_keys("neha")
#         password_input.send_keys("Neha@123")

#         # Wait for the login button to be clickable
#         login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
#         login_button.click()

#         # Redirect to the dashboard URL after successful login
#         dashboard_url = self.live_server_url + "/dashboard"
#         self.driver.get(dashboard_url)

#Login testing ends    



from django.test import TestCase
# from django.urls import reverse
# from home.models import CustomUser  # Import your CustomUser model

# class YourTest(TestCase):
#     def setUp(self):
#         # Create a custom user
#         self.user = CustomUser.objects.create_user(
#             username='admin', email='admin@gmail.com', password='Ajce24@mca')

#     def test_login(self):
#         # Attempt to log in
#         login_url = reverse('login')  # Replace with your login URL name
#         data = {'username': 'admin', 'password': 'Ajce24@mca'}
#         response = self.client.post(login_url, data)
        
#         # Check if login was successful (you might have different response codes or redirects)
#         self.assertEqual(response.status_code, 200)  # Replace 200 with the expected status code

#     def test_add_product(self):
#         # Assuming authenticated user, add a product
#         add_product_url = reverse('addequip')  # Replace with your add product URL name
#         data = {
#             'name': 'Product Name',
#             'rating': 5,
#             'description': 'Product Description',
#             # Add other required fields as needed
#         }
        
#         # Log in the user first
#         self.client.login(username='admin', password='Ajce24@mca')
#         response = self.client.post(add_product_url, data)
        
#         # Check if adding product was successful (add appropriate checks)
#         self.assertEqual(response.status_code, 200)  # Replace 200 with the expected status code

#     def test_view_equipments(self):
#         # Assuming authenticated user, attempt to view equipments
#         view_equip_url = reverse('view_equip')  # Replace with your view equipments URL name
        
#         # Log in the user first
#         self.client.login(username='admin', password='Ajce24@mca')
#         response = self.client.get(view_equip_url)
        
#         # Check if viewing equipments was successful (add appropriate checks)
#         self.assertEqual(response.status_code, 200)  # Replace 200 with the expected status code


# from django.test import TestCase
# from django.urls import reverse
# from home.models import CustomUser  # Import your CustomUser model

# class YourTest(TestCase):
#     # def setUp(self):
#     #     # Create a custom user
#     #     self.user = CustomUser.objects.create_user(
#     #         username='admin', email='admin@gmail.com', password='Ajce24@mca')

#     def test_login_then_add_product_then_view_equip(self):
#         # Attempt to log in
#         login_url = reverse('login')  # Replace with your login URL name
#         data = {'username': 'admin', 'password': 'Ajce24@mca'}
#         response = self.client.post(login_url, data, follow=True)

#         # Check if login was successful
#         self.assertEqual(response.status_code, 200)  # Expecting a successful login

#         # Follow the redirects to find the final URL
#         final_url = response.request.get("PATH_INFO", "")  # Fetch the final URL after redirects

#         # Now, add a product
#         add_product_url = reverse('addequip')  # Replace with your add product URL name
#         product_data = {
#             'name': 'Product Name',
#             'rating': 5,
#             'description': 'Product Description',
#             # Add other required fields as needed
#         }
#         add_product_response = self.client.post(add_product_url, product_data, follow=True)

#         # Check if adding product was successful
#         self.assertEqual(add_product_response.status_code, 200)  # Expecting a successful page load

#         # Check if the viewequip.html page is loaded successfully
#         view_equip_url = reverse('view_equip')  # Replace with your viewequip URL name
#         view_equip_response = self.client.get(view_equip_url)

#         # Check if viewing equipments was successful
#         self.assertEqual(view_equip_response.status_code, 200)  # Expecting a successful page load


# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from django.test import LiveServerTestCase


# class ProductAdditionTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.driver = webdriver.Chrome()
#         cls.driver.get(cls.live_server_url + "/login.html")



#     def test_login_then_add_product(self):
#         # Fill in login details and submit the form
#         username_input = self.driver.find_element(By.NAME, 'arya')
#         password_input = self.driver.find_element(By.NAME, 'Arya@123')

#         username_input.send_keys("arya")
#         password_input.send_keys("Arya@123")

#         submit_button = self.driver.find_element(By.XPATH, "//button[@type='Add Product']")
#         submit_button.click()

#         # Assuming successful login, proceed to add a product
#         product_name_input = self.driver.find_element(By.NAME, 'productName')
#         product_name_input.send_keys("Sample Product")
#         # ... Fill in other product details similarly ...

#         # Example: Uploading an image
#         image_input = self.driver.find_element(By.NAME, 'productImage')
#         image_input.send_keys(r"C:\copy1\django_project\static\images\excavator.jpg")  # Replace with the path to your image

#         # Wait for elements to be interactive or visible
#         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='Add Product']")))

#         # Scroll to the submit button
#         submit_button = self.driver.find_element(By.XPATH, "//button[@type='Add Product']")
#         self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)

#         # Click on the submit button
#         submit_button.click()

#         # You can add assertions here to verify successful product addition, like checking for success messages or updated product lists

#     def tearDown(self):
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys  # Import the Keys module
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from django.test import LiveServerTestCase

# class SearchProductTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.driver = webdriver.Chrome()
#         cls.driver.maximize_window()

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         super().tearDownClass()

#     def test_search_product(self):
#         wait = WebDriverWait(self.driver, 20)  # Adjust timeout as needed

#         # Go to the login page
#         self.driver.get(self.live_server_url + "/login.html")

#         # Perform login actions (replace the ID and name attributes as needed)
#         username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#         password_input = self.driver.find_element(By.NAME, "password")

#         username_input.send_keys("neha")
#         password_input.send_keys("Neha@123")

#         login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
#         login_button.click()

#         # Wait for successful login and redirect to the dashboard
#         dashboard_url = self.live_server_url + "/dashboard"
#         wait.until(EC.url_to_be(dashboard_url))

#         # Navigate to the product page
#         self.driver.get(self.live_server_url + "/product")

#         # Perform product search (adjust the search element IDs accordingly)
#         search_bar = wait.until(EC.presence_of_element_located((By.ID, "search-bar")))
#         search_query = "Excavator"  # Replace with the desired search query
#         search_bar.send_keys(search_query)
#         search_bar.send_keys(Keys.RETURN)

#         # Wait for search results on the search result page (modify as per your search results structure)
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))

#         # Capture and print the search results (adjust the class name accordingly)
#         search_results = self.driver.find_elements_by_class_name("container")
#         for result in search_results:
#             print(result.text)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from django.test import LiveServerTestCase

# class LoginTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.driver = webdriver.Chrome()
#         cls.driver.maximize_window()

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         super().tearDownClass()

#     def test_login_successful_and_search_product(self):
#         wait = WebDriverWait(self.driver, 20)

#         # Go to the login page
#         self.driver.get(self.live_server_url + "/login.html")

#         # Perform login actions
#         username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#         password_input = self.driver.find_element(By.NAME, "password")

#         username_input.send_keys("neha")
#         password_input.send_keys("Neha@123")

#         login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
#         login_button.click()

#         # Wait for successful login
#         dashboard_url = self.live_server_url + "/dashboard"
#         self.driver.get(dashboard_url)  # Adjust based on the URL pattern

#         # Navigate to the product page
#         self.driver.get(self.live_server_url + "/product")

#         # Perform product search
#         search_bar = wait.until(EC.presence_of_element_located((By.ID, "search-bar")))
#         search_query = "Excavator"  # Replace with the desired search query
#         search_bar.send_keys(search_query)
#         search_bar.send_keys(Keys.RETURN)

#         # Wait for search results on the search result page
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))

#         # Capture and print the search results
#         search_results = self.driver.find_elements_by_class_name("container")
#         for result in search_results:
#             print(result.text)



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from django.test import LiveServerTestCase
from selenium.common.exceptions import StaleElementReferenceException

class LoginTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_login_successful_and_search_product(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        driver.get(self.live_server_url + "/login.html")

        # Perform login actions
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "password")

        username_input.send_keys("neha")
        password_input.send_keys("Neha@123")

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
        login_button.click()

        # Wait for successful login
        dashboard_url = self.live_server_url + "/dashboard"
        driver.get(dashboard_url) 

        # Navigate to the product search page
        driver.get(self.live_server_url + "/search_blog?csrfmiddlewaretoken=m00rTjelqKHY8QIrrYZwkb13bNJcumfNTP7lPwKiochzwGeH4Nf3Vbd8MXMAi0wL&q=Excavator")

        # Wait for search results on the search result page
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))

        # Capture and print the search results
        search_results = driver.find_elements(By.CLASS_NAME, "container")
        for result in search_results:
            print(result.text)
