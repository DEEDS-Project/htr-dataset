DEEDS HTR Dataset
=================

![characters badge](badges/characters.svg) ![regions badge](badges/regions.svg) ![lines badge](badges/lines.svg) ![files badge](badges/files.svg)

A collection of transcriptions for medieval cartularies written in Latin used in the training of HTR models to read medieval texts. 

## Context / Project
- This repository houses a compilation of transcriptions from medieval cartularies written in Latin, specifically curated to serve as training data for HTR models dedicated to deciphering medieval charter texts written in Latin. 
- This dataset was created using eScriptorium, as an interface for HTR ground truth production, and Kraken, an HTR and layout engine. 
- Composed of primarily English cartulary material ranging from the 9th - 16th Centuries 
- More of a focus on material from the 10th - 15th centuries, to develop the machine’s capacity to read more complex scripts (compared to earlier scripts which the machine already performs relatively well on) 
- Dataset is mostly made from pre-existing transcriptions 
  - Supplemented with machine-generated transcriptions that were corrected manually
- This dataset is comprised of transcription data from the following cartularies/manuscripts:
  - British Library, Cotton MS Nero E VI 
  - Bibliothèque Virtuelle des Manuscrits Médiévaux, Cartulaire de l'abbaye du Mont-Saint-Michel, AVRANCHES, Bibliothèque municipale, 0210, 1154-1158
  - Bodleian Library, Founder's and Benefactors' book of Tewkesbury Abbey, Bodleian Library MS. Top. Glouc. d. 2, 16th century 
  - Christ Church Library, Cartulary of Eynsham Abbey, Christ Church MS 341, 1196–1197
  - Thomas Fisher Rare Book Library, Confirmatio chartarum, Charta de foresta, et alia statuta regum Henrici III, Edwardi I, et Edwardi II, fisher2:134, 1316-1422
  - British Library, Cartulary of Reading Abbey, Egerton MS 3031, 1190-1199
  - Archives Departementales de Saone-et-Loire, Cartulary of the bishopric of Autun, G 443, 13th century 
  - Trinity College Dublin, Cartulary of Torre Abbey, IE TCD MS 524, 13th century 

## Dataset

| Shelfmark                                                         | Holding Institution                                                                                                                                                      | Century                                                                                           | Script                                              | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [British Library, MS_Nero E VI](./data/bl-cotton-nero-e-vi)       | [British Library]()                                                                                                                                                      | Secretary (double compartimented a, looped d and tironian et, forked r, final s is a closed loop) | 200r-204r; 205r; 206r-209r; 210r; 211r; 212r; 213r; | Cartulary of the Order of the Hospital of St. John of Jerusalem in England (title); behalf of the prior and brethen of the Hospital of St. John of Jerusalem and begun under Grand Prior Robert Botyll (produced on); Clerkenwell, Essex, England (composed at); Latin (language); vellum (material). Content: Prima Camera of the Hospitaller Cartulary (ff. 3-288), counties: Reynham (200r), Morehall (200v), Westhurrok/Purflete (201-203v), Turrok Grey (204), Chaureth (205-214v). Two hands: first hand until fol. 204 (Turrok Grey), second hand from Chaureth (205r). |
| [AVRANCHES, Bibliothèque municipale, 0210](./data/avranches-0210) | [Bibliothèque Virtuelle des Manuscrits Médiévaux](https://iiif.biblissima.fr/collections/manifest/9c1850d8799e1c2e44330b3e3f0f37bfd420ec72?tify={%22view%22:%22info%22}) | Praegothica                                                                                       | 5r-9v                                               | Cartulaire du Mont Saint Michel (title); montois monk or abbot (author); Mont St Michel, France (composed at); Latin (language); parchment (material). Content: original part of the cartulary (ff. 1-108), literary text of the Revelatio (ff. 5-10).                                                                                                                                                                                                                                                                                                                         |
| [Bodleian Library MS. Top. Glouc. d. 2](./data/bod-top-glouc-d-2) | [Oxford Library](https://digital.bodleian.ox.ac.uk/objects/d3ea83dc-d2aa-4012-aa5b-2f9ba06ef6c1/)                                                                        | 6v-7v; 12r: Secretary. 9r-11v: imitates at 13th c. hand: cursiva anglicana imitation              | 6v-7v; 9r-12r                                       | Founder's and benefactors' book of Tewkesbury Abbey (title); several hands; Tewkesbury, Gloucestershire, Benedictine abbey of St Mary the Virgin, England (composed at); Latin (language); parchment (material). Charter of William fitz Count, with his portrait (ff.6-7v); Chronicle of founders and benefactors (ff. 8-40v).                                                                                                                                                                                                                                                |
| [Christ Church MS 341](./data/ccl-341)                            | [Christ Church, University of Oxford](https://digital.bodleian.ox.ac.uk/objects/7a841ab1-883a-41ce-a421-d8afc162a5e7/)                                                   | Late protogotic bookhands                                                                         | 11r; 13v-14r; 15v, 16r; 21r                         | Cartulary of Eynsham Abbey (title); Monks of Eynsham (authors); Eynsham, England (composed at); Latin (language); parchment (material). Rubric: Carta Regis Æthelredi de fundatione huius Ecclesie (ff. 7-45), cartulary of Eynsham abbey.                                                                                                                                                                                                                                                                                                                                     |

## Collaborators

- École Pratique des Hautes Études
- École Nationale des Chartes 
- ALMAnaCH, Inria

## Funding

This project is funded by the Social Sciences and Humanities Research Council of Canada (SSHRCC), under the project “Text as Image, Image as Text: Charter integrity and topic modelling”, an Insight Grant under the code 1350911. 

Additional funding is provided by the University of Toronto’s Work-Study program through its Career & Co-Curricular Learning Network.


## Transcription guidelines

The transcription guidelines are described in a paper available on [HAL](https://hal-enc.archives-ouvertes.fr/hal-03828353): the project follows the guidelines from the CREMMA Medieval datasets.
