#importing necessary modules
import os, requests, bs4, lxml, time
main_url = "https://quotes.toscrape.com/page/{}/"

#creating a func to clear screen
def clear_screen():
    return os.system('cls')

#page selector
def page_selector():

    page_num = ''

    while not str(page_num).isdigit():
        try:
            page_num = int(input("\nPlease enter the page number to selected."))

        except:
            print("\tInvalid input. Try againn.")
            continue
        
        else:
            clear_screen()
            print(f"\nChecking if data available on page '{page_num}'.")

            #activating web scrapping:
            url = main_url.format(page_num)
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, 'lxml')
            
            if [quote for quote in quotes(soup)] == []:
                print("\nNo data found! Please select another page.")
                return page_selector()

            else:
                print("\nData found. Can begin scrapping!")
                return soup, page_num

#func to print the authors
def authors(soup):
    for author in soup.select(".author"):
        yield author.text
    
#func to print the quotes
def quotes(soup):
    for quote in soup.select(".text"):
        yield quote.text

#func to print top ten tags on the page
def top_ten_tags(soup):
    top_ten_tags = [tag.text for tag in soup.select('.tag-item .tag')]
    return top_ten_tags

#a timer function
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'\nTime taken to execute: {end - start}')
    return wrapper

#using decorator timer func with func to print unique authors from the entire website
@timer
def unique_authors():

    unique_authors_list = []
    page = 1
    
    while True:
        
        print(f"\nChecking page: {page}")
        
        url = main_url.format(page)
        print(f"\nChecking URL: {url}")
        
        request = requests.get(url)
    
        try:
            soup = bs4.BeautifulSoup(request.text, 'lxml')
            
            #raise exception is no quotes found, meaning end of page
            if [quote for quote in quotes(soup)] == []:
                raise Exception("\nException Found!")
                
        except Exception:
            print("No quotes found!")
            break
    
        else:
            author_list = [author for author in authors(soup)]
            if author_list:
                print("\nAuthors found:")
                print(author_list)
                unique_authors_list.extend(author_list)
            
            page += 1
            continue
            
    #waiting for 2s then clearing screen
    print("Clearing screen in 2s.")
    time.sleep(2)
    clear_screen()

    print(f"\nTotal number of authors: {len(unique_authors_list)}")
    print(f"\nTotal number of unique authors: {len(set(unique_authors_list))}")
    print("\nFollowing is the list of all the unique authors on the website:")

    for author in sorted(list(set(unique_authors_list))):
        print('*', author)

#option selector
def option_selector():
    
    options_text = {1: "Print the authors on the page.", 2: "Print the quotes on the page.", \
    3: "Print the top ten tags on the page.", 4: "Print authors and quotes together for the page.", \
    5: "Print all the unique authors from all the pages."}
    
    print('\n')
    for item in options_text:
        print(f'{item}. {options_text[item]}')
    
    option = 0
    
    while option not in range(1,6) or not str(option).isdigit():
        try:
            option = int(input("\nPlease enter the number for the option to be selected."))
            
            if option not in range(1,6):
                print("\tNo such option available currently. Please try again.")
                continue

        except:
            print("\tInvalid input. Please try again.")
            continue
        
        else:
            clear_screen()
            print(f'\nYou have selected option:\n|----->{options_text[option]}')
            return option

#main execution
if __name__ == "__main__":

    #introduction
    print("\nThis is a 'Web Scrapping' example app.\nTesting website: https://quotes.toscrape.com/")
    print("\nThe website has multiple quotes from various authors.\nYou can perform operations like getting authors or quotes from a given page.")
    print("Check the available options later.\n")

    #loop for the entire scrapper
    scrapper_on = True

    while scrapper_on:
        
        soup, page_num = page_selector()
        
        #loop for option selection
        option_selection_on = True

        while option_selection_on:

            option = option_selector()
   
            if option == 1:
                print(f"\nFollowing are the authors found on page '{page_num}':")
                for pos, author in enumerate(authors(soup)):
                    print(f'{pos+1}. {author}')

            elif option == 2:
                print(f"\nFollowing are the quotes found on page '{page_num}':")
                for pos, quote in enumerate(quotes(soup)):
                    print(f'{pos+1}. {quote}')

            elif option == 3:
                print(f"\nFollowing are the top ten tags found on '{page_num}':")
                for pos, tags in enumerate(top_ten_tags(soup)):
                    print(f'{pos+1}. {tags}')

            elif option == 4:
                print(f"\nFollowing the author-quotes found on the page '{page_num}':")
                author, quote = '', ''
                for pos, item in enumerate(zip(authors(soup), quotes(soup))):
                    author, quote = item
                    print(f'\n{pos+1}. {quote} - {author}')
            
            elif option == 5:
                clear_screen()
                print(f"\nFor this option, authors are being scrapped from all the working pages on the website.")
                print("\nStarting in 2s.")
                time.sleep(2)
                unique_authors()

            #asking to continue scrapping on the given page with said options		
            keep_scrapping = ''
            
            while keep_scrapping.lower() not in ['y', 'n']:
                keep_scrapping = input("\nDo you want to continue to scrap on the same page?\nPress 'Y' for 'Yes' or 'N' for 'No'.")

                if keep_scrapping.lower() not in ['y', 'n']:
                    print("\tInvalid input. Please try again.")
                    continue

                elif keep_scrapping.lower() == 'y':
                    option_selection_on = True
                    print("\nPlease continue then.")
                    break
 
                elif keep_scrapping.lower() == 'n':
                    close_app = ''
                    
                    while close_app.lower() not in ['y', 'n']:
                        close_app = input("\nDo you want to close the Web Scrapping application? Enter 'Y' for 'Yes' or 'N' for 'No.")
                        
                        if close_app.lower() not in ['y', 'n']:
                            print("\tInvalid input. Please try again.")
                            continue
                        
                        if close_app.lower() == 'y':
                            print("\nThank you for trying this application. Have a nice day!")
                            option_selection_on = False
                            scrapper_on = False
                            break
                        
                        elif close_app.lower() == 'n':
                            print("\nIn this case, please select another page to scrap.")
                            option_selection_on = False
                            scrapper_on = True
                            break


