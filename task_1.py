'''
    У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників 
    у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, 
    які розділені комою без пробілів.
        Example:
        Alex Korp,3000
        Nikita Borisenko,2000
        Sitarama Raju,1000

    Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає 
    загальну та середню суму заробітної плати всіх розробників.

'''
# Format file, reason: I have generated the file with the wrong format
def format_file(input_path: str, output_path: str) -> int:

    with open(input_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for i in range(0, len(data), 2):
                name_line = data[i].strip()
                salary_line = data[i+1].strip()
                
                name, last_name = name_line.split(' ')
                new_line = f'{last_name},{name},{salary_line}\n'
                output_file.write(new_line)
    return 0           

format_file('./salary_data.txt', './salary_data_formatted.txt') 

# Calculate total salary and average salary
def total_salary(path: str) -> tuple:
    '''
        Function to calculate total salary and average salary
        
        :param path: str: path to the file
        :return: tuple: total salary and average salary (total, average)
    '''
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                if (line.strip() == ''):
                    continue
                _, _, salary = line.strip().split(',')
                total += int(salary)
                count += 1
                
            if count == 0:
                print('No data found')
                return (0, 0) 

            return total, total / count
    except FileNotFoundError:
        print(f'File not found: {path}')
        return (0, 0)
    except Exception as e:
        print(f'Error: {e}')
        return (0, 0)

total, average = total_salary("./salary_data_formatted.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")