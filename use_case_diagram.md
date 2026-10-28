flowchart LR
    P([Patient])
    D([Doctor])
    
    subgraph MediCare
        UC1[View doctor availability]
        UC2[Book appointment]
        UC3[Accept or decline appointment]
        UC4[Enforce appointment limit]
        UC5[Notify appointment status]
    end
    
    P --- UC1
    P --- UC2
    UC3 --- D
    UC4 -.->|"«extend»"| UC2
    UC5 -.->|"«extend»"| UC3