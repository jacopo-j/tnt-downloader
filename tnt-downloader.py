#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# © 2017 Jacopo Jannone


from __future__ import print_function  # For those still using Python 2
import sys
import requests
from lxml import html
from time import sleep
import os
import re
import argparse
import colorama
from colorama import Fore, Style
from terminaltables import SingleTable
try:
    import readline
except ImportError:
    # readline does not exist on Windows
    pass
try:
   input = raw_input # If we are on Python 2
except NameError:
   pass


# Strings and constants
progr_desc = "Cerca e scarica torrent da TNTVillage."
query_desc = "termine di ricerca"
more_desc = "mostra 21 risultati per pagina anzi che 7."
search_url = "http://www.tntvillage.scambioetico.org/src/releaselist.php"
tot_pag_addr = "//div[@class='pagination']/form/span/b[3]/text()"
result_table_addr = "//div[@class='showrelease_tb']/table/tr"
title_addr = "./td[7]/a/text()"
desc_addr = "./td[7]/text()"
leech_addr = "./td[4]/text()"
seed_addr = "./td[5]/text()"
dl_addr = "//div[@class='showrelease_tb']/table/tr[{}]/td[1]/a/@href"
title_str = Style.BRIGHT + "{}" + Style.RESET_ALL + "\n" + Style.DIM + "{}" + Style.RESET_ALL + "{}"
count_str = Style.BRIGHT + "{:02}" + Style.RESET_ALL
seed_str = Style.BRIGHT + Fore.GREEN + "{}" + Style.RESET_ALL
leech_str = Style.BRIGHT + Fore.MAGENTA + "{}" + Style.RESET_ALL
# dloading_str = "Download del file {} di {} in corso..."
# Per stampare anche il nome del file in corso di download oltre al numero
dloading_str = "Download del file {} di {} - {}..."
loading_str = "Caricamento dati in corso..."
prompt_dl = "[#] Download / [q] Esci: "
prompt_dl_next = "[#] Download / [s] Successivo / [q] Esci: "
prompt_dl_prev = "[#] Download / [p] Precedente / [q] Esci: "
prompt_dl_prev_next = "[#] Download / [p] Precedente / [s] Successivo / [q] Esci: "
no_results_str = Fore.RED + "La ricerca non ha prodotto nessun risultato." + Fore.RESET
table_header = [Style.BRIGHT + "#" + Style.RESET_ALL, Style.BRIGHT + "L" + Style.RESET_ALL, Style.BRIGHT + "S" + Style.RESET_ALL, Style.BRIGHT + "Titolo" + Style.RESET_ALL]
next_keys = ("s", "S")
prev_keys = ("p", "P")
quit_keys = ("q", "Q")
all_keys = next_keys + prev_keys + quit_keys
if (os.name != 'nt'):
    _, columns = os.popen('stty size', 'r').read().split()
else:
    con_data = os.popen("mode con", "r").read()
    cols = con_data.split("\n")[4]
    columns = re.findall(" *.+: *(\d+)", cols)[0]


def valid_dl(value, start, stop):
    # Returns true if ALL of the comma-separated numbers input by the
    # user are within the range of the displayed items.
    if (value == -1):
        return False
    for i in [x.strip() for x in value.split(",")]:
        try:
            if not (start <= int(i) < stop):
                return False
        except ValueError:
            return False
    return True


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def str_fit(string, width):
    # Adapts a string to fit a certain width
    if (len(string) <= width):
        return string + " " * (width - len(string))
    return string[:(width - 3)] + "..."


def do_search(search_input, chunks_size):
    # Core function. Searches TNT for the input string, shows the result
    # on screen, and parses the next action.
    try:
        count = 1
        cur_page = 1
        cur_chunk = 0
        results_per_chunk = 0
        page_back = False  # Needed afterwards
        chunk_back = False  # Also needed afterwards
        result_rows = {}  # We use a dict to associate the numbers
                          # shown next to each result with the actual
                          # row number of that result in the table
                          # parsed from TNT.

        while True:
            command = -1  # What the user wants to do after the results
                          # are shown
            prev_count = count
            if (cur_chunk == 0) and not (chunk_back):
                print(loading_str)
                result = requests.post(
                    search_url,
                    data={"cat": "0",
                          "page": cur_page,
                          "srcrel": search_input})
                search_tree = html.fromstring(result.content.decode('utf-8'))

                # Total number of pages we got from our search
                tot_pages = int(search_tree.xpath(tot_pag_addr)[0])

                # Results table
                table = search_tree.xpath(result_table_addr)

                if (len(table) <= 1):
                    # If there are no results
                    print(no_results_str)
                    break

                # We split each page into several "chunks", with
                # chunks_size results each. This is done so that the
                # result screen is easier to read and the user doesn't
                # need to scroll up and down.
                chunks = []
                alt_count = count
                for idx, row in enumerate(table):
                    if (idx == 0):
                        # The first row of the table is the header. We
                        # can ignore it.
                        continue
                    if (((idx - 1) % chunks_size) == 0):
                        chunks.append([])
                    chunks[-1].append(row)
                    result_rows[alt_count] = idx + 1
                    alt_count += 1

            clear_terminal()

            if (page_back):
                # Explanation below
                cur_chunk = len(chunks) - 1

            table_data = [table_header]
            title_width = float("inf")

            for row in chunks[cur_chunk]:
                # Table width check
                prev_title_width = title_width
                leech = row.xpath(leech_addr)[0].strip()
                seed = row.xpath(seed_addr)[0].strip()
                count_space = len(str(count))
                if (count_space <= 1):
                    count_space = 2
                leech_space = len(leech)
                if (leech_space <= 1):
                    leech_space = 2
                seed_space = len(seed)
                if (seed_space <= 1):
                    seed_space = 2
                title_width = min(
                    int(columns)
                        - (count_space + leech_space + seed_space + 13),
                    prev_title_width)

            for idx, row in enumerate(chunks[cur_chunk]):
                # Actual table formatting
                if (sys.version_info.major == 2):
                    # If we are on Python 2, we need to encode the
                    # title and description strings to utf-8.
                    title = row.xpath(title_addr)[0].replace(u'\xa0', u"").encode("utf-8").strip()
                    desc = row.xpath(desc_addr)[0].replace(u'\xa0', u"").encode("utf-8").strip()
                else:
                    title = row.xpath(title_addr)[0].strip()
                    desc = row.xpath(desc_addr)[0].strip()

                title_ell = str_fit(title, title_width)
                desc_ell = str_fit(desc, title_width)

                if (idx == len(chunks[cur_chunk]) - 1):
                    separator = ""
                else:
                    separator = "\n"

                leech = row.xpath(leech_addr)[0].strip()
                seed = row.xpath(seed_addr)[0].strip()

                table_data.append([
                    count_str.format(count),
                    leech_str.format(int(leech)),
                    seed_str.format(int(seed)),
                    title_str.format(title_ell, desc_ell, separator)])

                count += 1

            table = SingleTable(table_data)
            table.justify_columns[0] = "right"
            table.justify_columns[1] = "right"
            table.justify_columns[2] = "right"
            print(table.table)

            results_per_chunk = len(chunks[cur_chunk])

            if (len(chunks) == 1) and (tot_pages == 1):
                # If there is only one chunk and one page the user can
                # only choose what to download.
                while (not valid_dl(command, prev_count, count)
                       and (command not in quit_keys)):
                    command = input(prompt_dl).strip()
            else:
                if (cur_chunk == 0) and (cur_page == 1):
                    # Else, if we are displaying the first chunk on the
                    # first page, the user can either choose what do
                    # download or go to the next chunk.
                    while (not valid_dl(command, prev_count, count)
                           and (command not in next_keys + quit_keys)):
                        command = input(prompt_dl_next).strip()

                elif ((cur_chunk == len(chunks) - 1)
                      and (cur_page == tot_pages)):
                    # If we are displaying the last chunk on the last
                    # page, the user can either choose what to download
                    # or go to the previous chunk.
                    while (not valid_dl(command, prev_count, count)
                           and (command not in prev_keys + quit_keys)):
                        command = input(prompt_dl_prev).strip()
                else:
                    # Else, the user can choose what do wonload or go
                    # to the next or previous chunk.
                    while (not valid_dl(command, prev_count, count)
                           and (command not in all_keys)):
                        command = input(prompt_dl_prev_next).strip()

            page_back = False  # Just bear with me for a moment
            chunk_back = False  # Ditto
            if (command in next_keys):
                # Let's go to the next chunk or page.
                if (cur_chunk == len(chunks) - 1):
                    cur_page += 1
                    cur_chunk = 0
                else:
                    cur_chunk += 1
                clear_terminal()

            elif (command in prev_keys):
                # Let's go to the previous chunk or page.
                if (cur_chunk == 0):
                    cur_page += -1
                    # The flag below is needed so that the function
                    # knows that we went back from page x to page x-1.
                    # This way, we know that after downloading the page
                    # x-1 we must set the current chunk to the last one
                    # of that page.
                    page_back = True
                else:
                    cur_chunk += -1
                    # Similarly, the flag below is needed so that the
                    # function knows it does not have to re-download the
                    # page after we went back from chunk 1 to chunk 0 of
                    # the same page.
                    chunk_back = True
                count += -chunks_size - results_per_chunk
                clear_terminal()

            elif valid_dl(command, prev_count, count):
                # Let's download things.
                dl_list = [int(x.strip()) for x in command.split(",")]
                wait_needed = False  # See below
                clear_terminal()
                for idx, i in enumerate(dl_list):
                    if (wait_needed):
                        # TNT strictly controls every request sent to
                        # their servers. If we request multiple files
                        # within a very short period of time, our IP
                        # address will get banned from TNT. So, after
                        # downloading our first file, we wait for a few
                        # seconds before downloading the next one.
                        sleep(2)
                    
                    dl_url = search_tree.xpath(
                        dl_addr.format(result_rows[i]))[0]
                    result = requests.get(dl_url)
                    disp = result.headers['content-disposition']

                    # We get the filename so that we can save the file
                    # with the correct name.
                    fname = re.findall(
                        "filename=(.+)", disp)[0].split("; ")[0][1:-1]

                    # La modifica permette di stampare il nome del file in download e non solo il numero
                    print(dloading_str.format(idx + 1, len(dl_list), fname))
                    
                    with open(fname, "wb") as outfile:
                        outfile.write(result.content)
                    wait_needed = True

                # We're done. Exit the loop and quit.
                break

            elif (command in quit_keys):
                clear_terminal()
                break

    except (KeyboardInterrupt, EOFError) as _:
        # On CTRL+C we do a clean exit
        clear_terminal()
        sys.exit(0)


def main():
    # initialize colorama
    colorama.init()

    # Parse command line arguments
    parser = argparse.ArgumentParser(description=progr_desc)
    parser.add_argument("query", metavar="query", type=str, help=query_desc)
    parser.add_argument("-m", "--more", action="store_true", help=more_desc)
    args = parser.parse_args()
    if (args.more):
        chunks_size = 21
    else:
        chunks_size = 7
    do_search(args.query, chunks_size)


if __name__ == "__main__":
    main()
