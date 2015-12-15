public class Problem1 extends Specification {
	
	public Problem1(){
		super();
		this.param = new int[3];
	}
	
	public String template(){
		return "Find the equation of the line with slope " + param[0] + " and "
				+ "passing through point (" + param[1] + ", " + param[2] + ")";
	}
	
	public boolean constraints(){
		boolean b1 = -100 <= param[0] && param[0] <= 100;
		boolean b2 = -100 <= param[1] && param[1] <= 100;
		boolean b3 = -100 <= param[2] && param[2] <= 100;
		boolean b4 = param[0] * param[1] != param[2];
		return b1 & b2 & b3 & b4;
	}
	
	public boolean correct(){
		return output[1]*param[1] + output[2]*param[2] == output[0] &&
				(double) param[0] == (double) output[1]/output[2];
	}
	
	public int[][] bounds(){
		int[][] intervals = new int[param.length][2];
		intervals[0] = new int[]{-100, 100};
		intervals[1] = new int[]{-100, 100};
		intervals[2] = new int[]{-100, 100};
		return intervals;
	}
}
