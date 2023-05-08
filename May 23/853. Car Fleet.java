import java.util.Arrays;
import java.util.Stack;

class Car {
    int position;
    double time;

    public Car(int position, double time) {
        this.position = position;
        this.time = time;
    }
}
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
            int n = position.length;
        if (n == 0) {
            return 0;
        }

        Car[] cars = new Car[n];
        for (int i = 0; i < n; i++) {
            double time = (double)(target - position[i]) / speed[i];
            cars[i] = new Car(position[i], time);
        }

        Arrays.sort(cars, (a, b) -> b.position - a.position);

        Stack<Car> stack = new Stack<>();
        stack.push(cars[0]);
        int fleetCount = 1;

        for (int i = 1; i < n; i++) {
            if (cars[i].time > stack.peek().time) {
                stack.push(cars[i]);
                fleetCount++;
            }
        }

        return fleetCount;
    }
}
