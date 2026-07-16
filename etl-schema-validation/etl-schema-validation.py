def validate_records(records, schema):
    """
    Validate records against a schema definition.
    """
    # Write code here
    
    output_list=[]
    for i,r in enumerate(records):
        errors=[]

        for entry in schema:
            val = r.get(entry["column"],None)
            if entry["column"] not in r:
                errors.append(f"{entry["column"]}: missing")
                continue
            
            if val is None:
                if not entry["nullable"]:
                    errors.append(f"{entry["column"]}: null")
                continue
            else:
                if entry["type"] == "float":
                    type_mismatch = type(val).__name__ not in ("float", "int")
                else:
                    type_mismatch = type(val).__name__ != entry["type"]
                if type_mismatch :
                    errors.append(f"{entry["column"]}: expected {entry["type"]}, got {type(val).__name__}")
                    continue
    
                if "min" in entry and "max" in entry and(entry["min"] > val or entry["max"] < val ):
                    errors.append(f"{entry["column"]}: out of range")
                    continue


        output_list.append((i,len(errors)==0,errors))


    return output_list
            
        