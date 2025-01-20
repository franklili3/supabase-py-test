# Schema
```sql
CREATE TABLE "test3" (
    "accumulated_blocks" INTEGER PRIMARY KEY
);
```

# Policy
```
alter policy "Enable insert for authenticated users only"
on "public"."test3"
to authenticated
with check (
  true
);
```

# Environment
```
conda create -n p310 python=3.10
conda activate p310
pip install supabase
```

# Run
```
python insert_test.py
```

# Output
```
(p310) C:\myprojects\github\supabase-py-test>python insert_test.py
row_json:  {"accumulated_blocks": 879707}
Traceback (most recent call last):
  File "C:\myprojects\github\supabase-py-test\insert_test.py", line 38, in <module>
    raise Exception(f"Failed to post data: {response3_json}")
Exception: Failed to post data: {'data': [], 'count': None}
```
