public class palavraPalindromo {
    public static void main(String[] args) {
       String palavra = "ARARA";
       String resultado=""; 
        for(int x=palavra.length()-1;x>=0;x--){
            resultado+= palavra.charAt(x);
        }
        if(resultado.equals(palavra)){
            System.out.println("A palavra "+palavra+ " é um PALINDROMO");
        }else{
            System.out.println("A palavra "+palavra+ " NÃO é um PALINDROMO");;
        }
    }
}
