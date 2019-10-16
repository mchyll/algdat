package Oving7;

import org.omg.CORBA.INTERNAL;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.stream.Stream;

public class Oving7 {
    public static void main(String[] args) throws Exception {
        Stream<String> lineStream = Files.lines(Paths.get("C:\\L7Skandinavia-navn"));
        ArrayList<String> lines = new ArrayList<>();
        lineStream.forEach(lines::add);
        int numNames = Integer.parseInt(lines.get(0).trim());
        lines.remove(0);
        HashMap<Integer, String> names = new HashMap<>(numNames);
        lines.forEach(line -> {
            String[] parts = line.trim().split("\\s+");
            names.put(Integer.parseInt(parts[0]), parts[2]);
        });

        lineStream = Files.lines(Paths.get("C:\\L7Skandinavia"));
        lines = new ArrayList<>();
        lineStream.forEach(lines::add);
        String[] num = lines.get(0).trim().split("\\s+");
        int numNodes = Integer.parseInt(num[0]);
        int numEdges = Integer.parseInt(num[1]);
        lines.remove(0);
        Graph graph = new Graph(numNodes);
        for (int i = 0; i < graph.nodes.length; i++) {
            String name = names.containsKey(i) ? names.get(i) : "" + i;
            graph.nodes[i] = new GraphNode(name);
        }

        lines.forEach(line -> {
            String[] parts = line.trim().split("\\s+");
            int fromNode = Integer.parseInt(parts[0]);
            int toNode = Integer.parseInt(parts[1]);
            graph.nodes[fromNode].edges.add(graph.nodes[toNode]);
        });

        GraphNode node = graph.nodes[1234];
        System.out.println(node.label + " har " + node.edges.size() + " veier fra seg");
    }
}

class Graph {
    GraphNode[] nodes;

    Graph(int numNodes) {
        nodes = new GraphNode[numNodes];
    }
}

class GraphNode {
    String label;
    UnorderedLinkedList edges;

    GraphNode(String label) {
        this.label = label;
        edges = new UnorderedLinkedList();
    }

    GraphNode() {
        this("");
    }
}

class UnorderedLinkedList {

    LinkedListNode head;

    LinkedListNode add(Object value) {
        LinkedListNode newNode = new LinkedListNode(value);
        newNode.next = head;
        head = newNode;
        return newNode;
    }

    void remove(LinkedListNode node) {

    }

    int size() {
        int i = 0;
        LinkedListNode current = head;
        while (current != null) {
            i++;
            current = current.next;
        }
        return i;
    }
}

class LinkedListNode {
    LinkedListNode next;
    Object value;

    LinkedListNode(Object value) {
        this.value = value;
    }
}