from webapp.models import Situation

Situations = [
    
Situation(
    question="Quand je me lève, je dois :",
    first_choice="Eteindre les lumières quand je change de pièce.",
    first_choice_electric_charge =48,
    seconde_choice="Garder toutes les pièces allumées parce que j’ai peur du noir.",
    seconde_choice_electric_charge = 2400,
    third_choice="Me rendormir",
    third_choice_electric_charge = 3000,
    right_answer="Eteindre les lumières quand je change de pièce.",
    category="Eclairage",
    advice ="En éteignant les lumières quand on change de pièce, on évite de consommer de l'électricité inutilement. Une ampoule à incandescence de 60 W consomme environ 0,06 kWh par heure. Si on laisse une ampoule allumée pendant 8 heures par jour, cela représente une consommation de 0,48 kWh par jour. En éteignant l'ampoule quand on quitte la pièce, on peut donc économiser jusqu'à 20 % de la consommation électrique de cette ampoule."
),

Situation(
    question="Quand je pars de chez moi :",
    first_choice="Je garde mes appareils en veille branchés.",
    first_choice_electric_charge =2400,
    seconde_choice="J’éteins tous mes appareils.",
    seconde_choice_electric_charge = 0,
    third_choice="Je garde mes appareils allumés",
    third_choice_electric_charge = 2400,
    right_answer="J'éteins tous mes appareils.",
    category="Appareils Electriques",
    advice ="Explication : Les appareils en veille consomment de l'électricité, même lorsqu'ils sont éteints. Une télévision en veille consomme environ 10 W. Un ordinateur en veille consomme environ 5 W. Si on laisse un ordinateur et une télévision en veille pendant 12 heures par jour, cela représente une consommation de 0,12 kWh par jour. En éteignant complètement les appareils, on peut donc économiser jusqu'à 20 % de la consommation électrique de ces appareils.",
),

Situation(
    question="Que faut-il faire avec le chauffe-eau pour réduire la consommation d'électricité ?",
    first_choice="Je règle la température de mon chauffe-eau électrique entre 50°C et 60°C.",
    first_choice_electric_charge =2250,
    seconde_choice="Je règle la température de mon chauffe-eau électrique entre 90°C et 100°C.",
    seconde_choice_electric_charge = 2900,
    third_choice="Je laisse allumé mon chauffe-eau électrique lorsque je pars en vacances ou pour une absence prolongée.",
    third_choice_electric_charge = 3450,
    right_answer="Je règle la température de mon chauffe-eau électrique entre 50°C et 60°C.",
    category="Eau chaude sanitaire",
    advice ="Je règle la température de mon chauffe-eau électrique entre 50°C et 60°C.Cela permet de limiter la consommation d'électricité nécessaire pour chauffer l'eau.",
),

Situation(
    question="Quand j’arrive au travail avec ma voiture électrique à 7h : ",
    first_choice="Je recharge ma voiture quand j’arrive au travail.",
    first_choice_electric_charge =4000,
    seconde_choice="J’attends 10h pour la charger.",
    seconde_choice_electric_charge = 2000,
    third_choice="Je ne la charge pas.",
    third_choice_electric_charge = 0,
    right_answer="J’attends 10h pour la charger.",
    category="Véhicule electrique",
    advice =" Recharger une voiture électrique consomme de l'électricité. Une voiture électrique moyenne consomme environ 0,3 kWh par heure pour se recharger. Si on recharge une voiture électrique pendant 8 heures par jour, cela représente une consommation de 2,4 kWh par jour. En attendant de recharger la voiture électrique entre 00h et 6h du matin  , on peut donc économiser jusqu'à 10 % de la consommation électrique de la recharge.",
),

Situation(
    question="Quand il fait chaud : ",
    first_choice="Je climatise directement la pièce.",
    first_choice_electric_charge =2000,
    seconde_choice="Lorsqu'il fait chaud, je baisse mes stores ou je ferme les volets la journée.",
    seconde_choice_electric_charge = 400,
    third_choice="Je pense à fermer mes fenêtres dès que la température extérieure dépasse celle de la pièce.",
    third_choice_electric_charge = 700,
    right_answer="Lorsqu'il fait chaud, je baisse mes stores ou je ferme les volets la journée.",
    category="Ventilation & climatisation",
    advice ="La climatisation consomme de l'électricité. Une climatisation moyenne consomme environ 2 kWh par heure. Si on climatise une pièce pendant 8 heures par jour, cela représente une consommation de 16 kWh par jour. En fermant les portes entre les pièces et en baissant les stores ou en fermant les volets, on peut donc économiser jusqu'à 20 % de la consommation électrique de la climatisation."
),
Situation(
    question="Quand j’allume le climatiseur : ",
    first_choice="Je descends au minimum le climatiseur.",
    first_choice_electric_charge =1500,
    seconde_choice="Je garde allumé mon climatiseur quand je change de pièce pour ne pas perdre le frais.",
    seconde_choice_electric_charge = 2000,
    third_choice="Je règle ma climatisation pour avoir une température 4 à 6 °C plus basse que la température extérieure mais jamais inférieure à 25 °C.",
    third_choice_electric_charge = 1000,
    right_answer="Je règle ma climatisation pour avoir une température 4 à 6 °C plus basse que la température extérieure mais jamais inférieure à 25 °C.",
    category="Ventilation & climatisation",
    advice ="En descendant au minimum le climatiseur, on consomme toujours de l'électricité. Cependant, on consomme moins d'électricité qu'en réglant le climatiseur à une température plus élevée.",
),

Situation(
    question="Quand je rentre chez moi avec ma voiture électrique à 18h : ",
    first_choice="Je recharge immédiatement ma voiture électrique.",
    first_choice_electric_charge =4000,
    seconde_choice="J’attends cette nuit pour la charger.",
    seconde_choice_electric_charge = 2000,
    third_choice="Je ne la charge pas ",
    third_choice_electric_charge = 0,
    right_answer="J’attends cette nuit pour la charger.",
    category="Véhicule electrique",
    advice =" Recharger une voiture électrique consomme de l'électricité. Une voiture électrique moyenne consomme environ 0,3 kWh par heure pour se recharger. Si on recharge une voiture électrique pendant 8 heures par jour, cela représente une consommation de 2,4 kWh par jour. En attendant de recharger la voiture électrique entre 00h et 6h du matin  , on peut donc économiser jusqu'à 10 % de la consommation électrique de la recharge.",

),

Situation(
    question="Quand je cuisine : ",
    first_choice="Je garde la plaque électrique allumée jusqu’à la fin de la cuisson.", 
    first_choice_electric_charge =3000,
    seconde_choice="J’utilise de préférence un four classique plutôt qu’un four à micro-onde.", 
    seconde_choice_electric_charge = 1300,
    third_choice="Je sors mes aliments du réfrigérateur 5 minutes avant la cuisson.", 
    third_choice_electric_charge = 1000,
    right_answer="Je sors mes aliments du réfrigérateur 5 minutes avant la cuisson.", 
    category="Cuisson",
    advice ="En gardant la plaque électrique allumée jusqu'à la fin de la cuisson, on consomme plus d'électricité que si on l'éteignait dès que la cuisson est terminée."
),


Situation(
    question="Quand il fait froid chez moi :",
    first_choice="Je règle la température de mon chauffage entre 26 et 29 degrés dans la journée et à 21 degrés la nuit",
    first_choice_electric_charge =3000,
    seconde_choice="Je règle la température de mon chauffage entre 19 et 21 degrés dans la journée et à 17 degrés la nuit.",
    seconde_choice_electric_charge = 1500,
    third_choice="Je le laisse allumé pendant que je suis au travail",
    third_choice_electric_charge = 9000,
    right_answer="Je règle la température de mon chauffage entre 19 et 21 degrés dans la journée et à 17 degrés la nuit.",
    category="chauffage",
    advice="En réglant la température du chauffage entre 19 et 21 degrés dans la journée et à 17 degrés la nuit, on consomme moins d'électricité qu'en réglant la température à une valeur plus élevée.",
),

Situation(
    question="Que faut-il faire avec le chauffe-eau pour réduire la consommation d’électricité ?:",
    first_choice="Je règle la température de mon chauffe-eau électrique entre 50°C et 60°C.",
    first_choice_electric_charge =1500,
    seconde_choice="Je règle la température de mon chauffe-eau électrique entre 90°C et 100°C.",
    seconde_choice_electric_charge = 3000,
    third_choice="Je laisse allume mon chauffe-eau électrique lorsque je pars en vacances ou pour une absence prolongée.",
    third_choice_electric_charge = 8000,
    right_answer="Je règle la température de mon chauffe-eau électrique entre 50°C et 60°C.",
    category="chauffage",
    advice = "Je règle la température de mon chauffe-eau électrique entre 50°C et 60°C.Cela permet de limiter la consommation d'électricité nécessaire pour chauffer l'eau."
    
),

Situation(
    question="Le froid électroménager consomme beaucoup d’énergie. Quel geste adopteriez-vous pour économiser la consommation d’énergie ?",
    first_choice="Je place mon réfrigérateur ou mon congélateur à côté des appareils de cuisson pour consommer moins d'énergie.",
    first_choice_electric_charge =1200,
    seconde_choice="Je place mon réfrigérateur ou mon congélateur assez loin des appareils de cuisson pour consommer moins d'énergie.",
    seconde_choice_electric_charge = 700,
    third_choice="Je règle le réfrigérateur entre 0 °C et -5 °C et le congélateur à -18 °C.",
    third_choice_electric_charge = 2000,
    right_answer="Je place mon réfrigérateur ou mon congélateur assez loin des appareils de cuisson pour consommer moins d'énergie.",
    category="Froid",
    advice ="les avantages de placer votre réfrigérateur ou votre congélateur assez loin des appareils de cuisson sont les suivants :Réduction de la consommation d'énergie : En réduisant la quantité de chaleur absorbée, vous pouvez réduire la consommation d'énergie de votre réfrigérateur ou de votre congélateur de 10 à 20 %.Amélioration de la performance : Le réfrigérateur ou le congélateur peut fonctionner plus efficacement, ce qui peut prolonger sa durée de vie.",
),
Situation(
    question="Le lave-linge et le lave-vaisselle sont gourmands en consommation d’énergie. Parmi les solutions ci-dessus, laquelle adopteriez-vous pour réduire la consommation d’énergie de ces machines.",
    first_choice="Je privilégie les hautes températures qui sont souvent suffisamment efficaces.",
    first_choice_electric_charge =4000,
    seconde_choice="Je privilégie l'usage de mon sèche-linge plutôt que le séchage à l’air libre",
    seconde_choice_electric_charge = 3500,
    third_choice="J'utilise les programmes « Eco » de mon lave-linge et de mon lave-vaisselle.",
    third_choice_electric_charge = 1200,
    right_answer="J'utilise les programmes « Eco » de mon lave-linge et de mon lave-vaisselle.",
    category="Lavage",
    advice="En utilisant les programmes « Eco » de votre lave-linge et de votre lave-vaisselle, vous pouvez réduire votre consommation d'électricité de 20 à 30 %.",
),



]