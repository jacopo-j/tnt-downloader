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
pip install future lxml requests
git clone https://github.com/jacopo-j/tnt-downloader.git
cd tnt-downloader
chmod +x ./tnt-downloader.py
```

## Installazione su Windows

* Scaricare ed installare [Python](http://www.python.it/download/), preferibilmente Python 3. **IMPORTANTE: durante l'installazione selezionare la casella *Add Python to PATH***;
* riavviare il computer (consigliato);
* scaricare questo repository come file zip cliccando sul bottone verde nella parte in alto a destra della pagina;
* estrarre il file zip in una cartella;
* eseguire il file `tntdl-win-setup.bat`;
* per eseguire lo script, aprire il file `tnt-downloader.bat`.

## Utilizzo

Lo script si utilizza passando come argomento la stringa da cercare su TNTVillage. I risultati vengono mostrati sotto forma di elenco numerato e sono suddivisi in pagine.

Per scaricare uno o più torrent tra quelli mostrati, scrivere i relativi numeri separati da una virgola. Per passare alla pagina successiva scrivere `s`; per tornare alla precedente `p`.

Di default lo script mostra 7 risultati per pagina in modo da agevolarne la visualizzazione. Se utilizzate un terminale più grande del normale, potreste voler aumentare il numero dei risultati per pagina. Potete farlo utilizzando l'opzione `-m` quando eseguite lo script.

## Esempio

<pre>
utente@host:~$ ./tntsearch.py "rick and morty"

Caricamento dati in corso...

[01]	<b>Rick and Morty S03E01</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[720p - H264 - Eng Ac3 - Softsub Ita Eng] HDTVrip

[02]	<b>Rick and Morty S02E01-10</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bdrip 720p - H264 - Ita Eng Ac3 - Softsub Ita Eng]

[03]	<b>Rick and Morty S02e01-10</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[H264 - Eng Aac - SoftSub Ita Eng]  Animation

[04]	<b>Rick and Morty S01E07-11</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BDMux 1080p - H264 - Ita Eng Ac3 - Sub Ita Eng] Cosmic horror

[05]	<b>Rick and Morty S01E01-06</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BDMux 1080p - H264 - Ita Eng Ac3 - Sub Ita Eng] Cosmic horror

[06]	<b>Rick and Morty s01e01-11</b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[H264 - Eng Aac - SoftSub Ita Eng]  Animation

[0-9] Download: 2, 4

Download del file 1 di 2 in corso...
Download del file 2 di 2 in corso...</pre>

## Nota bene

* I server di TNT soffrono di problemi di sovraffollamento, quindi effettuano rigidi controlli sulle richieste effettuate. Troppe richieste in un arco di tempo ridotto comportano il ban del proprio indirizzo IP. Usate questo script con un minimo di buon senso.


* L'autore dello script non è in nessun modo affiliato o legato a TNTVillage. Non è stato autorizzato dai proprietari del sito a creare questo script e non l'ha fatto su richiesta o per conto dei suoi utenti.


* Questo script è un mezzo che semplifica il download di file da un sito web esterno. L'autore non si assume alcuna responsabilità e si dissocia completamente dalla natura e dal contenuto di questi file. Vedete questo script come una sorta di *browser alternativo*.


* Gli utenti sono responsabili delle azioni che effettuano con questo script. L'autore non si assume alcuna responsabilità se a causa di questo script si rompe qualcosa, si perdono dei dati, o se il vostro gatto prende fuoco. Se violate la legge utilizzando questo script, la responsabilità è vostra e solo vostra.
