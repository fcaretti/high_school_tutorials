import unicodedata
import string

lettere_italiane = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "Z", " "]

def pulisci_testo(testo):
    testo = testo.upper()
    testo = testo.replace("\n", " ")
    testo = ''.join(c for c in testo if c in lettere_italiane)
    testo = testo.replace("  ", " ")
    return testo

testo_originale = """Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita. 3
Ahi quanto a dir qual era é cosa dura
esta selva selvaggia e aspra e forte
che nel pensier rinova la paura! 6
Tant'é amara che poco é piu morte;
ma per trattar del ben chii' vi trovai,
dird de I'altre cose chii' v'ho scorte. 9
lo non so ben ridir comii' v'intrai,
tant'era pien di sonno a quel punto
che la verace via abbandonai. 12
Ma poi chii' fui al pié d'un colle giunto,
la dove terminava quella valle
che m'avea di paura il cor compunto, 15
guardai in alto e vidi le sue spalle
vestite gia de’ raggi del pianeta
che mena dritto altrui per ogne calle. 18
Allor fu la paura un poco queta,
che nel lago del cor m'era durata
la notte ch'i’ passai con tanta pieta. 21
E come quei che con lena affannata,
uscito fuor del pelago a la riva,
si volge a l'acqua perigliosa e guata, 24
cosi l'animo mio, ch'ancor fuggiva,
si volse a retro a rimirar lo passo
che non lascio gia mai persona viva. 27
Poi ch'éi posato un poco il corpo lasso,
ripresi via per la piaggia diserta,
si che 'I pié fermo sempre era ‘Il pil basso. 30
Ed ecco, quasi al cominciar de I'erta,
una lonza leggera e presta molto,
che di pel macolato era coverta; 33
e non mi si partia dinanzi al volto,
anzi ‘mpediva tanto il mio cammino,
chii' fui per ritornar pil volte volto. 36
Temp'era dal principio del mattino,
e 'l sol montava 'n su con quelle stelle
ch'eran con lui quando I'amor divino 39
mosse di prima quelle cose belle;
si ch'a bene sperar m'era cagione
di quella fiera a la gaetta pelle 42
l'ora del tempo e la dolce stagione;
ma non si che paura non mi desse
la vista che m‘apparve d'un leone. 45
Questi parea che contra me venisse
con la test'alta e con rabbiosa fame,
si che parea che l'aere ne tremesse. 48
Ed una lupa, che di tutte brame
sembiava carca ne la sua magrezza,
e molte genti fé gia viver grame, 51
questa mi porse tanto di gravezza
con la paura ch'uscia di sua vista,
ch'io perdei la speranza de I'altezza. 54
E qual é quei che volontieri acquista,
e giugne 'l tempo che perder lo face,
che 'n tutti suoi pensier piange e s'attrista; 57
tal mi fece la bestia sanza pace,
che, venendomi 'ncontro, a poco a poco
mi ripigneva la dove 'I sol tace. 60
Mentre ch'i' rovinava in basso loco,
dinanzi a li occhi mi si fu offerto
chi per lungo silenzio parea fioco. 63
Quando vidi costui nel gran diserto,
“Miserere dime”, gridai a lui,
“qual che tu sii, od ombra od omo certo!”. 66
Rispuosemi: “Non omo, omo gia fui,
e li parenti miei furon lombardi,
mantoani per patria ambedui.
Nacqui sub lulio, ancor che fosse tardi,
e vissi a Roma sotto '| buono Augusto
nel tempo de li déi falsi e bugiardi.
Poeta fui, e cantai di quel giusto
figliuol d'Anchise che venne di Troia,
poi che 'l superbo Ilién fu combusto.
Ma tu perché ritorni a tanta noia?
perché non sali il dilettoso monte
ch’é principio e cagion di tutta gioia?”.
“Or se’ tu quel Virgilio e quella fonte
che spandi di parlar si largo fiume?”,
rispuos'io lui con vergognosa fronte.
“O deli altri poeti onore e lume,
vagliami ‘I lungo studio e 'l grande amore
che m‘ha fatto cercar lo tuo volume.
Tu se' lo mio maestro e'l mio autore,
tu se’ solo colui da cu’ io tolsi
lo bello stilo che m'ha fatto onore.
Vedi la bestia per cu' io mi volsi;
aiutami da lei, famoso saggio,
ch'ella mi fa tremar le vene e i polsi”.
“A te convien tenere altro viaggio”,
rispuose, poi che lagrimar mi vide,
“se vuo' campar d'esto loco selvaggio;
ché questa bestia, per la qual tu gride,
non lascia altrui passar per la sua via,
ma tanto lo 'mpedisce che l'uccide;
e ha natura si malvagia e ria,
che mai non empie la bramosa voglia,
e dopo 'l pasto ha pit fame che pria.
Molti son li animali a cui s'ammoglia,
e pill saranno ancora, infin che 'I veltro
verra, che la fara morir con doglia.
Questi non cibera terra né peltro,
ma sapienza, amore e virtute,
e sua nazion Sara tra feltro e feltro."""

testo_pulito = pulisci_testo(testo_originale)
print(testo_pulito)
