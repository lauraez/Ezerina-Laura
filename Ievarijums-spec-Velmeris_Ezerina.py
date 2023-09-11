try:
      abolu_masa=float(input("ievadiet ābolu masu(kg):"))
      cukura_masa=float(input("ievadiet cukura masa(kg):"))

      print("""recepte 1l ievārījumam:
            āboli 1kg
            cukurs 1kg
            ūdens 1l""")
      
      def calcJam():#aprēķina ievārijuma tilpumu pēc ievadīto abolu un cukura daudzuma(receptes proporcijas ir 1:1:1, tādēļ tilpumu rēķina pēc mazākā)
            if abolu_masa<cukura_masa:
                  V_ievarijums = abolu_masa
            elif cukura_masa<abolu_masa:
                  V_ievarijums = cukura_masa
            return V_ievarijums#atgriež ievārijuma tilpumu
      
      def calcCost():#aprēķina ievārijuma cenu pēc ievadīto abolu un cukura daudzuma(receptes proporcijas ir 1:1:1, tādēļ cenu rēķina pēc mazākā)
            if abolu_masa<cukura_masa:
                  cena = abolu_masa
            elif cukura_masa<abolu_masa:
                  cena = cukura_masa
            print(f""""ievārījuma izmaksas
      ----------------------------------------------------
                  cukurs:{round(cena,2)}€
            
            """)#round(....,2) noapaļo float vērtību ar 2 cipariem aiz komata
      calcCost()
except ValueError:#ja ievadvērtība nav float, tad izdrukā šo tekstu
      print("datu tipi ir float")