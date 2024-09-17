bel = []
ger = [
    'der', 'die', 'das', 'ein', 'eine', 'und', 'oder', 'aber', 'sich', 'mit',
    'auf', 'von', 'zu', 'für', 'in', 'an', 'bei', 'über', 'nach', 'das',
    'den', 'des', 'dem', 'as', 'es', 'du', 'ich', 'wir', 'ihr', 'sie', 'mir',
    'dir', 'uns', 'euch', 'sich', 'ihn', 'ihr', 'sein', 'ihre', 'meine',
    'deine', 'unsere', 'eure', 'deren'
]

dan = [
    'og', 'i', 'er', 'på', 'at', 'til', 'det', 'en', 'af', 'med', 'som', 'for', 
    'den', 'de', 'har', 'man', 'der', 'var', 'jeg', 'du', 'vi', 'de', 'ham', 
    'hende', 'os', 'jer', 'dem', 'hvor', 'når', 'hvad', 'hvordan', 'hvilken', 
    'hvis', 'som', 'skal', 'kan', 'må', 'vil', 'jeg', 'du', 'vi', 'at', 'med', 
    'til', 'om', 'af', 'fra', 'på', 'over', 'under', 'mellem', 'ud', 'ind', 
    'gennem', 'op', 'ned', 'ud', 'i', 'til', 'fra', 'om', 'ved', 'fra', 'mod'
]

eng = [
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
    'any', 'are', 'aren\'t', 'as', 'at', 'be', 'because', 'been', 'before', 'being',
    'below', 'between', 'both', 'but', 'by', 'can', 'could', 'did', 'didn\'t', 'do',
    'does', 'doesn\'t', 'doing', 'don\'t', 'down', 'during', 'each', 'few', 'for',
    'from', 'further', 'had', 'hadn\'t', 'has', 'hasn\'t', 'have', 'haven\'t', 'having',
    'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if',
    'in', 'into', 'is', 'isn\'t', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma', 'me',
    'might', 'mightn\'t', 'more', 'most', 'must', 'mustn\'t', 'my', 'myself', 'need',
    'needn\'t', 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or',
    'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan\'t',
    'she', 'should', 'shouldn\'t', 'so', 'some', 'such', 't', 'than', 'that', 'the',
    'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this',
    'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was',
    'wasn\'t', 'we', 'were', 'weren\'t', 'what', 'when', 'where', 'which', 'while',
    'who', 'whom', 'why', 'will', 'with', 'won\'t', 'would', 'wouldn\'t', 'y',
    'you', 'your', 'yours', 'yourself', 'yourselves'
]

spa = [
    'a', 'al', 'algo', 'algún', 'alguna', 'algunas', 'alguno', 'algunos', 'an', 'ante',
    'antes', 'con', 'como', 'de', 'del', 'desde', 'donde', 'dos', 'el', 'ella', 'ellos',
    'en', 'entre', 'era', 'eres', 'es', 'ese', 'esa', 'eso', 'está', 'estamos', 'están',
    'este', 'esta', 'esto', 'fue', 'ha', 'has', 'hasta', 'he', 'la', 'las', 'le', 'les',
    'lo', 'los', 'me', 'mi', 'mis', 'mucho', 'muchos', 'muy', 'nada', 'ni', 'no', 'nos',
    'nuestro', 'nuestra', 'nuestros', 'nuestras', 'o', 'otro', 'otros', 'para', 'pero',
    'por', 'que', 'quien', 'qué', 'se', 'si', 'sí', 'solo', 'son', 'su', 'sus', 'tal',
    'también', 'te', 'tenemos', 'tenéis', 'tener', 'ti', 'todo', 'todos', 'tu', 'tus',
    'un', 'una', 'unos', 'usas', 'usted', 'ustedes', 'ya', 'yo'
]

fre = [
    'à', 'a', 'afin', 'avec', 'au', 'aucun', 'ce', 'cela', 'ces', 'cette', 'dans',
    'de', 'des', 'du', 'elle', 'en', 'est', 'et', 'être', 'eux', 'il', 'ils', 'je',
    'le', 'les', 'leur', 'lui', 'ma', 'maintenant', 'mais', 'me', 'moi', 'mon', 'ne',
    'nos', 'notre', 'nous', 'ou', 'par', 'pas', 'pour', 'qu', 'que', 'qui', 's', 'sa',
    'se', 'ses', 'soi', 'son', 'sur', 'ta', 'te', 'tes', 'toi', 'ton', 'tous', 'tout',
    'tu', 'un', 'une', 'va', 'vous', 'y', 'à', 'avec', 'c', 'comme', 'dans', 'de',
    'des', 'du', 'en', 'et', 'les', 'le', 'la', 'pour', 'qui', 'que', 'se', 'si',
    'sur', 'tous', 'très', 'à'
]

ita = [
    'a', 'abito', 'ad', 'al', 'alla', 'allo', 'anche', 'ancora', 'altri', 'aumentare',
    'aveva', 'bello', 'bene', 'c', 'come', 'con', 'da', 'dal', 'della', 'dello', 'di',
    'e', 'è', 'ed', 'effetto', 'fino', 'ha', 'ho', 'i', 'il', 'in', 'l', 'la', 'le', 
    'lo', 'ma', 'mi', 'mio', 'molto', 'nella', 'non', 'noi', 'nostro', 'nostri', 
    'nuovo', 'o', 'per', 'più', 'pochi', 'quale', 'questo', 'se', 'sì', 'sono', 
    'su', 'tanto', 'te', 'tra', 'tu', 'un', 'una', 'uno', 'è', 'voi', 'volte', 'za'
]

dut = [
    'aan', 'af', 'alle', 'alles', 'als', 'altijd', 'aan', 'bij', 'ben', 'bent', 'bij',
    'de', 'deze', 'die', 'dit', 'doch', 'eigen', 'en', 'er', 'had', 'heb', 'hebben',
    'heeft', 'hem', 'hen', 'hier', 'hij', 'hoe', 'ik', 'in', 'is', 'je', 'jij', 'jou',
    'jullie', 'kan', 'je', 'mij', 'met', 'me', 'men', 'mijn', 'moet', 'na', 'naar',
    'niet', 'nooit', 'nu', 'of', 'om', 'onder', 'onze', 'ons', 'ook', 'op', 'over',
    'reeds', 'samen', 's', 'soms', 'te', 'ten', 'tijdens', 't', 'uit', 'uw', 'van',
    'vanaf', 'veel', 'ver', 'voor', 'was', 'we', 'werd', 'willen', 'wilt', 'wij', 'zal',
    'ze', 'zijn', 'zich', 'zij', 'zo', 'zonder', 'de'
]

nor = [
    'og', 'i', 'til', 'den', 'det', 'en', 'et', 'de', 'er', 'på', 'med', 'for', 'som',
    'at', 'har', 'jeg', 'du', 'han', 'hun', 'vi', 'de', 's', 'som', 'kan', 'hva', 'når',
    'hvor', 'hvordan', 'hvorfor', 'der', 'eller', 'men', 'da', 'så', 'på', 'av', 'fra',
    'over', 'under', 'til', 'ved', 'om', 'uten', 'fra', 'de', 'et', 'med', 'en', 'da',
    'bare', 'så', 'nå', 'vår', 'sine', 'deres', 'uten', 'skal', 'må', 'tror', 'noe',
    'bare', 'må', 'nå', 'ut', 'inn', 'så', 'hva', 'også', 'vel', 'ingen', 'hver'
]

pol = [
    'a', 'aby', 'aczkolwiek', 'ale', 'all', 'am', 'an', 'and', 'and', 'ani', 'bardziej', 
    'by', 'był', 'była', 'było', 'byśmy', 'być', 'czy', 'dla', 'do', 'dziś', 'jego', 
    'jak', 'jakie', 'jaki', 'jest', 'jestem', 'jeśli', 'już', 'kiedy', 'kim', 'które',
    'który', 'm', 'ma', 'mają', 'me', 'mi', 'może', 'my', 'na', 'nam', 'nas', 'nawet',
    'nie', 'niego', 'nikt', 'niski', 'o', 'od', 'oraz', 'oraz', 'os', 'over', 'po', 
    'pod', 'przez', 'proszę', 's', 'się', 'są', 'ta', 'tak', 'tam', 'te', 'teraz', 
    'to', 'tob', 'tą', 'ty', 'u', 'w', 'wtedy', 'wszystko', 'wszystkich', 'z', 'za',
    'ze', 'zresztą'
]

por = [
    'a', 'ao', 'aos', 'aquela', 'aquelas', 'aquilo', 'aquele', 'aqueles', 'as', 'até',
    'com', 'como', 'da', 'das', 'de', 'dela', 'dele', 'demais', 'depois', 'desde', 'do',
    'dos', 'e', 'ela', 'elas', 'ele', 'eles', 'em', 'entre', 'era', 'es', 'essa', 'essas',
    'este', 'estes', 'eu', 'foi', 'foi', 'havia', 'a', 'me', 'minha', 'minhas', 'na', 'nas',
    'não', 'nas', 'nos', 'nós', 'o', 'os', 'para', 'pela', 'pelas', 'pelo', 'pelos', 'por',
    'qual', 'quando', 'que', 'quem', 's', 'se', 'sem', 'sua', 'suas', 'também', 'te', 'tem',
    'tenho', 'tinha', 'tirei', 'todos', 'uma', 'umas', 'você', 'vocês', 'a', 'o', 'um'
]

rus = []

swe = [
    'och', 'att', 'det', 'en', 'ett', 'i', 'på', 'av', 'för', 'till', 'med', 'som',
    'har', 'om', 'är', 'de', 'den', 'ett', 'så', 'för', 'vid', 'från', 'eller', 'då',
    'men', 'kan', 'alla', 'här', 'nu', 'var', 'så', 'vi', 'du', 'ni', 'han', 'hon',
    'vi', 'de', 'denna', 'detta', 'dessa', 'honom', 'henne', 'oss', 'er', 'era', 'måste',
    'utan', 'något', 'allt', 'var', 'efter', 'när', 'hur', 'varför', 'om', 'till', 'utan',
    'några', 'något', 'nu', 'där', 'här', 'under', 'över', 'genom', 'ut', 'in', 'upp',
    'ner'
]







