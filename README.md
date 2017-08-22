## Introduzione

`tnt-downloader` è uno script scritto in Python che permette di cercare e scaricare file torrent da [TNTVillage](http://tntvillage.scambioetico.org).

È stato creato per ovviare ai problemi di lentezza dei server di TNT che rendono estremamente frustrante navigare sul sito o sulla pagina di ricerca delle release.

## Compatibilità e requisiti

Questo script è stato testato su **macOS**, **Linux** e **Windows**. Dovrebbe essere compatibile con tutti i sistemi operativi purché sia presente **Python 2** o **Python 3** con i seguenti moduli installati:

* `future`
* `lxml`
* `requests`

## Installazione su macOS e Linux


```
git clone https://github.com/jacopo-j/tnt-downloader.git
cd tnt-downloader
pip install -r requirements.txt
chmod +x ./tnt-downloader.py
```

## Installazione su Windows

* Scaricare ed installare [Python](http://www.python.it/download/), preferibilmente Python 3. **IMPORTANTE: durante l'installazione selezionare la casella *Add Python to PATH***;
* riavviare il computer (consigliato);
* scaricare questo repository come file zip cliccando sul bottone verde nella parte in alto a destra della pagina;
* estrarre il file zip in una cartella;
* eseguire il file `tntdl-win-setup.bat` per installare automaticamente i moduli di Python richiesti.

Per una questione di praticità, si consiglia agli utenti Windows di eseguire lo script tramite il file `tntdl-windows.bat` invece che direttamente dal file dello script `tnt-downloader.py`.

## Utilizzo

Lo script si utilizza passando come argomento la stringa da cercare su TNTVillage. I risultati vengono mostrati sotto forma di tabella e sono suddivisi in pagine.

Le colonne della tabella mostrano, da sinistra a destra: il numero del torrent, il numero di leech, il numero di seed e il titolo del torrent.

Per scaricare uno o più torrent tra quelli mostrati nella tabella, scrivere i relativi numeri separati da una virgola. Per passare alla pagina successiva scrivere `s`; per tornare alla precedente `p`.

Di default lo script mostra 7 risultati per pagina in modo da agevolarne la visualizzazione. Se utilizzate un terminale più grande del normale, potreste voler aumentare il numero dei risultati per pagina. Potete farlo utilizzando l'opzione `-m` quando eseguite lo script.

## Esempio

<pre>
utente@host:~$ ./tnt-downloader.py "rick and morty"

Caricamento dati in corso...

┌────┬────┬────┬────────────────────────────────────────────────────────────────┐
│  <b>#</b> │  <b>L</b> │  <b>S</b> │ <b>Titolo</b>                                                         │
├────┼────┼────┼────────────────────────────────────────────────────────────────┤
│ <b>01</b> │  <span style="color:magenta"><b>1</b></span> │ <span style="color:green"><b>12</b></span> │ <b>Rick and Morty S03E01</b>                                          │
│    │    │    │ <span style="color:grey">[720p - H264 - Eng Ac3 - Softsub Ita Eng] HDTVrip</span>              │
│    │    │    │                                                                │
│ <b>02</b> │  <span style="color:magenta"><b>0</b></span> │ <span style="color:green"><b>10</b></span> │ <b>Rick and Morty S02E01-10</b>                                       │
│    │    │    │ <span style="color:grey">[Bdrip 720p - H264 - Ita Eng Ac3 - Softsub Ita Eng]</span>            │
│    │    │    │                                                                │
│ <b>03</b> │  <span style="color:magenta"><b>0</b></span> │  <span style="color:green"><b>3</b></span> │ <b>Rick and Morty S02e01-10</b>                                       │
│    │    │    │ <span style="color:grey">[H264 - Eng Aac - SoftSub Ita Eng]  Animation</span>                  │
│    │    │    │                                                                │
│ <b>04</b> │ <span style="color:magenta"><b>11</b></span> │ <span style="color:green"><b>24</b></span> │ <b>Rick and Morty S01E07-11</b>                                       │
│    │    │    │ <span style="color:grey">[BDMux 1080p - H264 - Ita Eng Ac3 - Sub Ita Eng] Cosmic horror</span> │
│    │    │    │                                                                │
│ <b>05</b> │ <span style="color:magenta"><b>11</b></span> │ <span style="color:green"><b>26</b></span> │ <b>Rick and Morty S01E01-06</b>                                       │
│    │    │    │ <span style="color:grey">[BDMux 1080p - H264 - Ita Eng Ac3 - Sub Ita Eng] Cosmic horror</span> │
│    │    │    │                                                                │
│ <b>06</b> │  <span style="color:magenta"><b>0</b></span> │  <span style="color:green"><b>7</b></span> │ <b>Rick and Morty s01e01-11</b>                                       │
│    │    │    │ <span style="color:grey">[H264 - Eng Aac - SoftSub Ita Eng]  Animation</span>                  │
└────┴────┴────┴────────────────────────────────────────────────────────────────┘
[0-9] Download: 2, 4

Download del file 1 di 2 in corso...
Download del file 2 di 2 in corso...</pre>

L'esempio rappresenta il download del secondo e del quarto torrent mostrati nella tabella.

## Nota bene

* I server di TNT soffrono di sovraffollamento, quindi effettuano rigidi controlli sulle richieste effettuate. Troppe richieste in un arco di tempo ridotto comportano il ban del proprio indirizzo IP. Usate questo script con un minimo di buon senso.


* L'autore dello script non è in nessun modo affiliato o legato a TNTVillage. Non è stato autorizzato dai proprietari del sito a creare questo script e non l'ha fatto su richiesta o per conto dei suoi utenti.


* Questo script è un mezzo che semplifica il download di file da un sito web esterno. L'autore non si assume alcuna responsabilità e si dissocia completamente dalla natura e dal contenuto di questi file. Vedete questo script come una sorta di *browser alternativo*.


* Gli utenti sono responsabili delle azioni che effettuano con questo script. L'autore non si assume alcuna responsabilità se a causa di questo script si rompe qualcosa, si perdono dei dati, o se il vostro gatto prende fuoco. Se violate la legge utilizzando questo script, la responsabilità è vostra e solo vostra.
