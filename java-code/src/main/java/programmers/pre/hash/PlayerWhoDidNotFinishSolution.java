package programmers.pre.hash;

import java.util.HashMap;
import java.util.Map;

public class PlayerWhoDidNotFinishSolution {
    public String solution(String[] participant, String[] completion) {
        if (participant.length < 1 || 100000 < participant.length)
            throw new IllegalArgumentException("1 <= participant <= 100000");
        if (participant.length - completion.length != 1)
            throw new IllegalArgumentException("completion + 1 = participant");

        String answer = "";

        Map<String, Integer> pMap = new HashMap<>();
        for (String p : participant) {
            int val = pMap.getOrDefault(p, 0);
            pMap.put(p, val <= 0 ? 1 : ++val);
        }
        for (String c : completion) {
            int val = pMap.get(c);
            pMap.put(c, --val);
        }
        for (Map.Entry<String, Integer> data : pMap.entrySet()) {
            if (data.getValue() != 0)   answer = data.getKey();
        }

        return answer;
    }
}