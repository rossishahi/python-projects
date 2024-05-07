#importing necessary modules
import os, re

def clear_screen():
	return os.system('cls')

def directory_confirm():
	main_dir = input("\nPlease copy-paste the main directory to be checked.")

	continue_or_not = ''
	
	while continue_or_not.lower() not in ['y', 'n']:

		continue_or_not = input("\nSelect 'Y' to proceed 'N' to update the directory.")

		if continue_or_not.lower() == 'y':
			main_dir = main_dir.replace('"', '')
			break
		
		elif continue_or_not.lower() == 'n':
			print("\n\tSure, please try again.")
			directory_confirm()
   
		else:
			print("\n\tIncorrect input. Please try again.")
			continue

	return main_dir

def pattern_confirm():
	pattern = input("\nPlease enter the pattern to be checked.")
	
	continue_or_not = ''

	while continue_or_not.lower() not in ['y', 'n']:

		continue_or_not = input("\nSelect 'Y' to proceed 'N' to update the pattern.")

		if continue_or_not.lower() == 'y':
			pattern = pattern.replace('"', '')
			break
		
		elif continue_or_not.lower() == 'n':
			print("\n\tSure, please try again.")		
			pattern_confirm()
   
		else:
			print("\n\tIncorrect input. Please try again.")
			continue

	return pattern

def find_pattern(main_dir, pattern):
    for dir, dir_name, files in os.walk(main_dir):
            for file in files:
                current_file_path = dir + '\\' + file
                updated_file_path = current_file_path.replace('\\', "\\\\")
                with open(updated_file_path, 'r') as text:
                    content = text.read()
                    value = re.findall(pattern, content)
                    if value:
                        print("\nMATCH FOUND FOR THE GIVEN PATTERN!")
                        print(f"\nFile path: {updated_file_path}")
                        print(f"\nResult: {value}")

if __name__ == '__main__':
	
	play = True
	
	print("Welcome to the 'Pattern Finder' app!")

	while play:

		main_dir = directory_confirm()
		pattern = pattern_confirm()

		clear_screen()
		find_pattern(main_dir, pattern)

		while True:
			again = input("\nDo you want to try another pattern? Press 'Y' or 'N' accordingly.")

			if again.lower() not in ['y', 'n']:
				print("\n\tIncorrect input. Please try again.")
				continue

			elif again.lower() == 'y':
				play = True
				print("\nStarting again!")
				clear_screen()
				break

			elif again.lower() == 'n':
				play = False
				print("\nThank you for trying the 'Pattern Finder' app.")
				break




