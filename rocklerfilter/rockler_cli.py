from rocklerscraper import RocklerScraper

def main():
    storeID = get_store_id()
    scraper = RocklerScraper(storeID)
    scraper.get_table(webpage=scraper.get_page(storeID))
    
    search_text = input("Enter Types of Wood You are Searching for, separated by commas:\n")
    min_inv  = get_value(default=1.0, msg="Enter the minimum inventory count of what you're looking for: ")
    max_price = get_value(default=100.0, msg="Enter the upper bound for the price range: ")
    board_search = get_bool(msg="Are you searching for Boards? Input 'y' if so. ")
    boardfeet_search = get_bool(msg="Are you searching for Board Feet? Input 'y' if so. ")
    
    data = scraper.filter_table(search_text, min_inv, max_price, 
                    board_search, boardfeet_search)
    print(data)

def get_store_id():
    return '04' #camdridge MA

def get_value(default:float, msg:str)->float:
    val = input(msg).strip()
    try:
        val = float(val)
    except ValueError:
        val = default
    return val

def get_bool(msg:str)->bool:
    val = input(msg)
    if val.lower().strip() == 'y':
        return True
    return False




