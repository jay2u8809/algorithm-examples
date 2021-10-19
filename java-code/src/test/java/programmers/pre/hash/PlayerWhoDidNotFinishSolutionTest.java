package programmers.pre.hash;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class PlayerWhoDidNotFinishSolutionTest {

    private PlayerWhoDidNotFinishSolution solution;

    @BeforeEach
    void before() {
        this.solution = new PlayerWhoDidNotFinishSolution();
    }

    @Test
    void solution_test() {
        // "leo"
        String[] participant = {"leo", "kiki", "eden"};
        String[] completion = {"eden", "kiki"};
        String result = this.solution.solution(participant, completion);
        System.out.println(result);

        // "vinko"
        participant = new String[]{"marina", "josipa", "nikola", "vinko", "filipa"};
        completion = new String[]{"josipa", "filipa", "marina", "nikola"};
        result = this.solution.solution(participant, completion);
        System.out.println(result);

        // "mislav"
        participant = new String[]{"mislav", "stanko", "mislav", "ana"};
        completion = new String[]{"stanko", "ana", "mislav"};
        result = this.solution.solution(participant, completion);
        System.out.println(result);
    }
}