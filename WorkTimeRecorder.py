import sys
import time
import re
from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side, Style, PatternFill, Alignment

from openpyxl.styles.colors import RED

reload(sys)
sys.setdefaultencoding('utf8')

headers = ['Date', 'Time (h)', 'Task', 'for whom? (mei62, Housing office, others)'];

class Entry:
    __entryCount = 0;
    def __init__(self, date, time, task, for_whom):
        self.date = date;
        self.time = time;
        self.task = task;
        self.for_whom = for_whom;
        self.__entryCount += 1;

def create_time_entry(date, time, task, for_whom):
    return Entry(date, time, task, for_whom);

def export_to_woko(entry_list):
    for entry in entry_list:
        return 1;
def print_line_in_workbook(entry):
    return 1;

def setup_default_layout(worksheet, entry_list):
    worksheet.cell('A3').value = 'WOKO Time recording';
    worksheet.cell('A3').font = Font(bold=True);
    for prefix in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        worksheet.cell(prefix + '3').fill = PatternFill(fill_type='solid', start_color='C0C0C0');
    worksheet.cell('A6').value = 'Student liaison assistant';
    worksheet.cell('A6').font = Font(bold=True);
    worksheet.cell('A7').value = 'Zhiyang Yu from ____ to _____';
    worksheet.cell('A7').font = Font(bold=True);
    worksheet.append(headers);
    worksheet.append(entry_list);
    for prefix in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        worksheet.cell(prefix + '20').border = Border(bottom=Side(border_style='thin'));
    worksheet.cell('A22').value = 'Total';
    worksheet.cell('A22').font = Font(bold=True);
    worksheet.cell('B22').value = 0.0;
    worksheet.cell('B22').font = Font(bold=True);
    worksheet.cell('B22').border = Border(bottom=Side(border_style='double'));
    worksheet.cell('B22').alignment = Alignment(horizontal='left');
    worksheet.cell('C22').value = 'hours';
    worksheet.cell('C22').border = Border(bottom=Side(border_style='double'));
    worksheet.cell('E22').value = 'Visa Head of Operations: ____________';
    worksheet.cell('A25').value = 'To be sent to the WOKO office until the 20th of each month (e-mail).';
    worksheet.cell('A25').font = Font(color=RED);

def setup_workbook(file_name, sheet_name, entry_list):
    workbook = Workbook();
    worksheet = workbook.worksheets[0];
    worksheet.title = sheet_name;
    total_hours = 0.0;
    setup_default_layout(worksheet, entry_list);
    save_path = file_name + '.xlsx';
    workbook.save(save_path);

if __name__=='__main__':
    setup_workbook("stundenliste china-tutorin1", "July",['2015-01-01']);