import webdriver_manager
import webdrivermanager
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())


driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get("https://google.com")

