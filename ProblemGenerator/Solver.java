
public class Solver {
	Specification spec;
	public Solver(Specification spec) {
		this.spec = spec;
	}
	
	public void setProblemParams(){
		int[][] bounds = spec.bounds();
		int[] params = new int[bounds.length];
		
		for (int i = 0; i < bounds.length; i ++){
			params[i] = (int) 
					(Math.random()*(bounds[i][1]-bounds[i][0]))+bounds[i][0];
		}
		spec.setParam(params);
	}
	
	public static void main(String[] args){
		Problem1 p = new Problem1();
		Solver s = new Solver(p);
		s.setProblemParams();
		System.out.println(p.template());
	}
}
