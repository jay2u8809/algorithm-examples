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

        // Solution 1
        for (Map.Entry<String, Integer> data : pMap.entrySet()) {
            if (data.getValue() != 0)   answer = data.getKey();
        }

        // Solution 2 (Best)
        for (Map.Entry<String, Integer> data : pMap.entrySet()) {
            if (data.getValue() == 0)   continue;
            answer = data.getKey();
            break;
        }

        // Solution 3
        for (String k : pMap.keySet()) {
            if (pMap.get(k) == 0)   continue;
            answer = k;
            break;
        }

        return answer;
    }
}