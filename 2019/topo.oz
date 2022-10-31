functor
import
    Application
    System
define

fun {Member Elem List}
    case List of nil then false
    [] H|T then
        if Elem == H then true
        else {Member Elem T} end
    end
end

proc {Visit Node Visited ?Sorted}
    {Member Node Visited} = false
    Sorted 
end

{System.show {Member 1 [2 1]}}

end