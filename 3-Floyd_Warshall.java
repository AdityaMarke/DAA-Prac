import java.util.Scanner;

class Floyd_Warshall{

    final static int INF = 99999;

    void MinTotalCost(int graph[][],int V){
        int dist[][] = new int[V][V];
        for(int i = 0 ; i < V ; i++){
            for(int j = 0 ; j < V ; j++){
                dist[i][j] = graph[i][j];
            }
        }

        for(int k = 0 ; k < V ; k++){
            for(int i = 0 ; i < V ; i++){
                for(int j = 0 ; j < V ; j++){
                    if(dist[i][k] != INF && dist[k][j] != INF){
                        dist[i][j] = Math.min(dist[i][j],dist[i][k] + dist[k][j]);
                    }
                }
            }
        }

        displaysol(dist,V);
    }

    void displaysol(int dist[][],int V){
        System.out.println("The matrix with minimum distance is :");

        for(int i = 0 ; i < V ; i++){
            for(int j = 0 ; j < V ; j++){
                if(dist[i][j] == INF)
                System.out.print("INF");
                else
                System.out.print(dist[i][j] + " ");
            }
            System.out.println();
        }
    }

        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of offices (vertices): ");
        int V = sc.nextInt();
        int graph[][] = new int[V][V];

        for(int i = 0 ; i < V ; i++){
            for(int j = 0 ; j < V ; j++){
                if(i==j)
                graph[i][j] = 0;
                else
                graph[i][j] = INF;
            }
        }

        while(true){
            System.out.print("Enter Source :");
            int s = sc.nextInt() - 1;
            if(s==-2)
            break;

            System.out.print("Enter Destination :");
            int d = sc.nextInt() - 1;
            if(d==-2)
            break;

            System.out.print("Enter Cost :");
            int cost = sc.nextInt();
            if(cost==-2)
            break;

            graph[s][d] = cost;
        }

        Floyd_Warshall fw = new Floyd_Warshall();
        fw.MinTotalCost(graph,V);
        sc.close();
    }

}
