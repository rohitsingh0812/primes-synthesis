
public abstract class Specification {
	public int[] param;
	public int[] output;
	
	
	public abstract String template();
	
	public void setOutput(int[] output){
		this.output = output;
	}
	
	public void setParam(int[] param){
		this.param = param;
	}
	
	public abstract boolean constraints();
	
	public abstract boolean correct();
	
	public abstract int[][] bounds();
}
