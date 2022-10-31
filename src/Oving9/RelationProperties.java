package Oving9;

class RelationProperties {
    /*
     * Assuming that a two column array containing the relation and a one column
     * array containing the set the relation is on is given in each method.
     * No checks are performed.
     */

    public static boolean isReflexive(char[][] relation, char [] set){
        for (char a : set) {
            boolean found = false;
            for (char[] aa : relation) {
                if (aa[0] == a && aa[1] == a) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                return false;
            }
        }
        return true;
    }

    public static boolean isSymmetric(char[][] relation, char [] set){
        for (char[] ab : relation) {
            boolean found = false;
            for (char[] ba : relation) {
                if (ab[0] == ba[1] && ab[1] == ba[0]) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                return false;
            }
        }
        return true;
    }

    public static boolean isTransitive(char[][] relation, char [] set){
        for (char[] ab : relation) {
            for (char[] bc : relation) {
                if (ab[1] == bc[0]) {
                    boolean found = false;
                    for (char[] ac : relation) {
                        if (ab[0] == ac[0] && bc[1] == ac[1]) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public static boolean isAntiSymmetric(char[][] relation, char [] set){
        for (char[] ab : relation) {
            for (char[] ba : relation) {
                if (ab[0] == ba[1] && ab[1] == ba[0] && ab[0] != ab[1]){
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean isEquivalenceRelation(char[][] relation, char [] set){
	    return isReflexive(relation, set) && isSymmetric(relation, set) && isTransitive(relation, set);
    }

    public static boolean isPartialOrder(char[][] relation, char [] set){
        return isReflexive(relation, set) && isAntiSymmetric(relation, set) && isTransitive(relation, set);
    }

    public static void main(String[] args) {
	char[] setA = {'a','x','r','m','2','0'};
	char[][] rel1 = {{'a','a'},{'r','a'},{'a','2'},{'x','x'},{'r','2'},{'r','r'},{'m','m'},{'2','r'},{'0','0'},{'a','r'},{'2','2'},{'2','a'}};
	char[][] rel2 = {{'a','x'},{'r','2'},{'0','0'},{'m','2'}};
	System.out.println("Rel1 is reflexive: " + isReflexive(rel1, setA));
	System.out.println("Rel2 is reflexive: " + isReflexive(rel2, setA));
	System.out.println("Rel1 is symmetric: " + isSymmetric(rel1, setA));
	System.out.println("Rel2 is symmetric: " + isSymmetric(rel2, setA));
	System.out.println("Rel1 is transitive: " + isTransitive(rel1, setA));
	System.out.println("Rel2 is transitive: " + isTransitive(rel2, setA));
	System.out.println("Rel1 is antisymmetric: " + isAntiSymmetric(rel1, setA));
	System.out.println("Rel2 is antisymmetric: " + isAntiSymmetric(rel2, setA));
	System.out.println("Rel1 is an equivalence relation: " + isEquivalenceRelation(rel1, setA));
	System.out.println("Rel2 is an equivalence relation: " + isEquivalenceRelation(rel2, setA));
	System.out.println("Rel1 is a partial order: " + isPartialOrder(rel1, setA));
	System.out.println("Rel2 is a partial order: " + isPartialOrder(rel2, setA));
	/* skal gi følgende utskrift:
	   Rel1 is reflexive: true
	   Rel2 is reflexive: false
	   Rel1 is symmetric: true
	   Rel2 is symmetric: false
	   Rel1 is transitive: true
	   Rel2 is transitive: true
	   Rel1 is antisymmetric: false
	   Rel2 is antisymmetric: true
	   Rel1 is an equivalence relation: true
	   Rel2 is an equivalence relation: false
	   Rel1 is a partial order: false
	   Rel2 is a partial order: false
	 */
    }


}
